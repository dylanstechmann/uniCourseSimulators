import test from 'node:test';
import assert from 'node:assert/strict';
import {freshState, sanitizeState, loadGuestState, STORAGE_KEY, BACKUP_KEY} from '../../legacy/src/state.js';

const storage = (initial = {}) => {
  const data = new Map(Object.entries(initial));
  return {getItem: key => data.has(key) ? data.get(key) : null, setItem: (key, value) => data.set(key, value), data};
};

test('legacy study data migrates without deletion', () => {
  const original = JSON.stringify({...freshState(), notes: {'cell-biology:0': 'Compare controls.'}, completed: {'cell-biology:0': true}, answers: {'cell-biology:0': {correct: true, value: 0, attempts: 1}}, bookmarks: ['cell-biology'], cardSchedule: {card: {dueAt: 1234, rating: 'good'}}});
  const store = storage({'lattice-academy:v1': original});
  const result = loadGuestState(store);
  assert.equal(result.notes['cell-biology:0'], 'Compare controls.');
  assert.equal(result.completed['cell-biology:0'], true);
  assert.equal(result.cardSchedule.card.rating, 'good');
  assert.equal(store.getItem('lattice-academy:v1'), original);
  assert.equal(store.getItem(BACKUP_KEY), original);
  assert.equal(JSON.parse(store.getItem(`${STORAGE_KEY}:migration`)).trust, 'unverified browser practice');
});

test('new state wins and backup remains', () => {
  const store = storage({[STORAGE_KEY]: JSON.stringify({...freshState(), notes:{new:'new'}}), 'lattice-academy:v1': JSON.stringify({notes:{old:'old'}}), [BACKUP_KEY]:'original'});
  assert.deepEqual(loadGuestState(store).notes, {new:'new'});
  assert.equal(store.getItem(BACKUP_KEY), 'original');
});

test('malformed persisted values cannot break reader', () => {
  for (const value of [null, [], 4, 'bad', {bookmarks:{}, notes:[], answers:'bad', completed:[]}, {cardSchedule:{a:{dueAt:'tomorrow',rating:'good'}}}]) {
    assert.deepEqual(loadGuestState(storage({[STORAGE_KEY]:JSON.stringify(value)})), freshState());
  }
  assert.deepEqual(loadGuestState(storage({[STORAGE_KEY]:'{broken'})), freshState());
  assert.deepEqual(loadGuestState({getItem(){throw new Error('blocked');}}), freshState());
});

test('rejects prototype keys, invalid records and oversized notes', () => {
  const input = JSON.parse('{"notes":{"__proto__":"bad","constructor":"bad","valid":"ok"},"answers":{"x":{"correct":true,"value":{},"attempts":1}},"bookmarks":["x","x",null]}');
  input.notes.huge = 'x'.repeat(100001);
  const result = sanitizeState(input);
  assert.deepEqual(result.notes,{valid:'ok'});
  assert.deepEqual(result.answers,{});
  assert.deepEqual(result.bookmarks,['x']);
  assert.equal({}.polluted, undefined);
});
