import { useState, type FormEvent } from "react";
import { api, errorMessage } from "../api";
import type { Session } from "../types";

export function AccountPanel({
  session,
  onSession,
}: {
  session: Session;
  onSession: (session: Session) => void;
}) {
  const [mode, setMode] = useState<"login" | "register">("register");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [message, setMessage] = useState("");
  const [busy, setBusy] = useState(false);
  const [deleteConfirmation, setDeleteConfirmation] = useState("");
  async function startGuest() {
    setBusy(true);
    setError("");
    try {
      onSession(await api.guest());
      setMessage(
        "Guest session started. You can now enroll and save your work.",
      );
    } catch (error) {
      setError(errorMessage(error));
    } finally {
      setBusy(false);
    }
  }
  async function authenticate(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setBusy(true);
    setError("");
    try {
      onSession(await api[mode](email, password));
      setPassword("");
      setMessage(
        mode === "register"
          ? "Account created. Existing guest work is retained."
          : "Signed in.",
      );
    } catch (error) {
      setError(errorMessage(error));
    } finally {
      setBusy(false);
    }
  }
  async function logout() {
    setBusy(true);
    setError("");
    try {
      await api.logout();
      onSession(await api.session());
      setMessage("Signed out.");
    } catch (error) {
      setError(errorMessage(error));
    } finally {
      setBusy(false);
    }
  }
  async function exportData() {
    setBusy(true);
    setError("");
    try {
      const data = await api.exportData();
      const url = URL.createObjectURL(
        new Blob([JSON.stringify(data, null, 2)], { type: "application/json" }),
      );
      const link = document.createElement("a");
      link.href = url;
      link.download = "lattice-courselab-learner-data.json";
      link.click();
      URL.revokeObjectURL(url);
      setMessage("Learner data exported. Keep the downloaded file private.");
    } catch (error) {
      setError(errorMessage(error));
    } finally {
      setBusy(false);
    }
  }
  async function deleteLearner(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (deleteConfirmation !== "DELETE") return;
    setBusy(true);
    setError("");
    try {
      await api.deleteLearner();
      onSession(await api.session());
      setDeleteConfirmation("");
      setMessage("Account and saved learner data deleted.");
    } catch (error) {
      setError(errorMessage(error));
    } finally {
      setBusy(false);
    }
  }
  return (
    <>
      <span className="eyebrow">Your learning space</span>
      <h1>Account and data</h1>
      {error && (
        <p className="error" role="alert">
          {error}
        </p>
      )}
      {message && (
        <p className="notice" role="status">
          {message}
        </p>
      )}
      {session.user && (
        <section className="card">
          <h2>{session.user.is_guest ? "Guest session" : "Signed in"}</h2>
          <p>
            {session.user.is_guest
              ? "Your server-saved guest work is tied to this browser session. Register to preserve account access, and export your work for a personal copy."
              : session.user.email}
          </p>
          <button onClick={logout} disabled={busy}>
            Sign out
          </button>
        </section>
      )}
      {(!session.user || session.user.is_guest) && (
        <div className="account-grid">
          <section className="card">
            <h2>{mode === "register" ? "Create an account" : "Sign in"}</h2>
            {session.user?.is_guest && (
              <p className="muted">
                Creating an account retains your current guest enrollments,
                notes, and attempts.
              </p>
            )}
            <form onSubmit={authenticate} className="stack">
              <label>
                Email address
                <input
                  type="email"
                  value={email}
                  onChange={(event) => setEmail(event.target.value)}
                  required
                  autoComplete="username"
                />
              </label>
              <label>
                Password
                <input
                  type="password"
                  value={password}
                  onChange={(event) => setPassword(event.target.value)}
                  required
                  minLength={12}
                  autoComplete={
                    mode === "register" ? "new-password" : "current-password"
                  }
                  aria-describedby="password-help"
                />
              </label>
              <small id="password-help">Use at least 12 characters.</small>
              <button className="primary" disabled={busy}>
                {busy
                  ? "Working…"
                  : mode === "register"
                    ? "Create account"
                    : "Sign in"}
              </button>
            </form>
            <button
              className="text-button"
              onClick={() => {
                setMode(mode === "register" ? "login" : "register");
                setError("");
              }}
              disabled={busy}
            >
              {mode === "register"
                ? "Use an existing account"
                : "Create a new account"}
            </button>
          </section>
          {!session.user && (
            <section className="card">
              <h2>Explore as a guest</h2>
              <p>
                Read the public catalog without signing in. Start a guest
                session to save enrollment, practice feedback, notes, bookmarks,
                and reading progress on this installation.
              </p>
              <button className="primary" onClick={startGuest} disabled={busy}>
                Start guest session
              </button>
              <p className="muted">
                Guest work is associated with the session cookie. Export it
                before leaving a shared device.
              </p>
            </section>
          )}
        </div>
      )}
      {session.user && (
        <div className="account-grid">
          <section className="card">
            <h2>Export your learner data</h2>
            <p>
              Download your account information, enrollments, practice attempts,
              notes, bookmarks, and reading progress as JSON.
            </p>
            <button onClick={exportData} disabled={busy}>
              Export learner data
            </button>
          </section>
          <section className="card danger">
            <h2>Delete account and data</h2>
            <p>
              This permanently deletes this account or guest session and all
              saved learner records on this installation. Export your work first
              if you want a copy.
            </p>
            <form onSubmit={deleteLearner} className="stack">
              <label>
                Type DELETE to confirm
                <input
                  value={deleteConfirmation}
                  onChange={(event) =>
                    setDeleteConfirmation(event.target.value)
                  }
                  autoComplete="off"
                />
              </label>
              <button
                className="danger-button"
                disabled={busy || deleteConfirmation !== "DELETE"}
              >
                Delete account and saved data
              </button>
            </form>
          </section>
        </div>
      )}
    </>
  );
}
