
const ApiBaseUrl = "http://127.0.0.1:8000/api/v1";

export async function Login(Email, Password) {
  const FormData = new URLSearchParams();

  FormData.append("username", Email);
  FormData.append("password", Password);

  const Response = await fetch(`${ApiBaseUrl}/auth/token`, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: FormData,
  });

  if (!Response.ok) {
    let ErrorMessage = "Login failed.";

    try {
      const ErrorData = await Response.json();

      if (typeof ErrorData.detail === "string") {
        ErrorMessage = ErrorData.detail;
      }
    } catch {
      // Keep the default error message.
    }

    throw new Error(ErrorMessage);
  }

  const Data = await Response.json();

  localStorage.setItem("AthenaeumAccessToken", Data.access_token);

  return Data;
}

export function GetAccessToken() {
  return localStorage.getItem("AthenaeumAccessToken");
}

export function Logout() {
  localStorage.removeItem("AthenaeumAccessToken");
}
