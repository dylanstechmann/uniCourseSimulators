import pytest

from courselab.content import ContentInvalid, ContentMissing, ContentRepository


def test_private_assessment_paths_are_confined_to_separate_read_root(tmp_path):
    public_root = tmp_path / "content"
    public_course = public_root / "courses" / "cell-biology"
    public_course.mkdir(parents=True)
    public_decoy = public_course / "answers.json"
    public_decoy.write_text('{"answer":"public decoy"}', encoding="utf-8")

    private_root = tmp_path / "private-assessments"
    private_file = private_root / "courses" / "cell-biology" / "assignments" / "homework-2.json"
    private_file.parent.mkdir(parents=True)
    private_file.write_text('{"answer":"private key"}', encoding="utf-8")

    repository = ContentRepository(public_root, private_root)
    assert repository.assessment_source_file(
        "cell-biology", "private://assignments/homework-2.json",
    ) == private_file.resolve()

    # A missing private mount cannot fall back to similarly named public content.
    without_private_root = ContentRepository(public_root)
    with pytest.raises(ContentMissing):
        without_private_root.assessment_source_file("cell-biology", "private://answers.json")

    for unsafe in (
        "private://../answers.json",
        "private:///absolute.json",
        "private://./answers.json",
        "private://assignments/../../answers.json",
        "private://assignments\\answers.json",
        "private://C:/outside.json",
    ):
        with pytest.raises(ContentInvalid):
            repository.assessment_source_file("cell-biology", unsafe)

    with pytest.raises(ValueError, match="separate roots"):
        ContentRepository(public_root, public_root / "private-assessments")


def test_private_assessment_symlink_cannot_escape_mount(tmp_path):
    public_root = tmp_path / "content"
    private_root = tmp_path / "private-assessments"
    course_root = private_root / "courses" / "cell-biology"
    course_root.mkdir(parents=True)
    outside = tmp_path / "outside.json"
    outside.write_text('{"answer":"outside"}', encoding="utf-8")
    link = course_root / "escape.json"
    try:
        link.symlink_to(outside)
    except (OSError, NotImplementedError):
        pytest.skip("Symlink creation is unavailable on this Windows host")

    repository = ContentRepository(public_root, private_root)
    with pytest.raises(ContentInvalid):
        repository.assessment_source_file("cell-biology", "private://escape.json")

    # The course directory itself must stay under the mount as well.
    second_private_root = tmp_path / "second-private-assessments"
    courses_root = second_private_root / "courses"
    courses_root.mkdir(parents=True)
    outside_course = tmp_path / "outside-course"
    outside_course.mkdir()
    (outside_course / "answer.json").write_text("{}", encoding="utf-8")
    try:
        (courses_root / "cell-biology").symlink_to(outside_course, target_is_directory=True)
    except (OSError, NotImplementedError):
        pytest.skip("Directory symlink creation is unavailable on this Windows host")

    repository = ContentRepository(public_root, second_private_root)
    with pytest.raises(ContentInvalid):
        repository.assessment_source_file("cell-biology", "private://answer.json")
