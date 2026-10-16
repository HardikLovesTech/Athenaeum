import { useState } from "react";
import { ArrowUpRight, BookOpen } from "lucide-react";

import { Login as LoginUser } from "../services/auth";

function Login({ OnLogin }) {
  const [Email, SetEmail] = useState("");
  const [Password, SetPassword] = useState("");
  const [ErrorMessage, SetErrorMessage] = useState("");
  const [IsLoading, SetIsLoading] = useState(false);

  async function HandleSubmit(Event) {
    Event.preventDefault();

    SetErrorMessage("");
    SetIsLoading(true);

    try {
      await LoginUser(Email, Password);
      OnLogin();
    } catch (Error) {
      SetErrorMessage(
        Error.message || "Unable to log in.",
      );
    } finally {
      SetIsLoading(false);
    }
  }

  return (
    <main className="LoginPage">
      <div className="LoginCard">
        <div className="LoginBrand">
          <BookOpen size={32} strokeWidth={1.8} />

          <div>
            <div className="BrandName">Athenaeum</div>
            <div className="BrandTagline">
              Your Knowledge. Amplified.
            </div>
          </div>
        </div>

        <div className="LoginHeader">
          <div className="LoginEyebrow">
            WELCOME BACK
          </div>

          <h1>Continue your research.</h1>

          <p>
            Sign in to access your documents and
            AI-powered research workspace.
          </p>
        </div>

        <form
          className="LoginForm"
          onSubmit={HandleSubmit}
        >
          <label>
            Email
            <input
              type="email"
              value={Email}
              onChange={(Event) =>
                SetEmail(Event.target.value)
              }
              placeholder="you@example.com"
              required
            />
          </label>

          <label>
            Password
            <input
              type="password"
              value={Password}
              onChange={(Event) =>
                SetPassword(Event.target.value)
              }
              placeholder="••••••••"
              required
            />
          </label>

          {ErrorMessage && (
            <div className="LoginError">
              {ErrorMessage}
            </div>
          )}

          <button
            className="LoginButton"
            type="submit"
            disabled={IsLoading}
          >
            {IsLoading ? "Signing in..." : "Sign in"}

            {!IsLoading && (
              <ArrowUpRight size={17} />
            )}
          </button>
        </form>
      </div>
    </main>
  );
}

export default Login;