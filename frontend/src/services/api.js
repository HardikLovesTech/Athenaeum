const ApiBaseUrl = "https://127.0.0.1:8000api/v1";

import { GetAccessToken } from "./auth";


async function ApiRequest(
  Endpoint,
  {
    Method = "GET",
    Body = null,
    Token = null,
    IsFormData = false,
  } = {},
) {
  const AccessToken = Token || GetAccessToken();

  const Headers = {};

  if (!IsFormData) {
    Headers["Content-Type"] = "application/json";
  }

  if (AccessToken) {
    Headers["Authorization"] = `Bearer ${AccessToken}`;
  }

  // ...
}

export async function GetKnowledgeItems(Token) {
    return ApiRequest("knowledge", {
        Method: "GET",
        Token,
    });
}

export async function UploadDocument(File, Token) {
    const FormData = new globalThis.FormData();

    FormData.append("File" , File);

    return ApiRequest("knowledge/upload",{
        Method: "POST",
        Body: FormData,
        Token,
        IsFormData: true,
    });
}


export async function AskDocuments(
    Query,
    KnowledgeItemId,
    Token,
) {
    return ApiRequest("/rag", {
        Method: "POST",
        Body: {
            Query,
            KnowledgeItemId,
        },
        Token,
    });
}

export async function GenerateSummary(
    KnowledgeItemId,
    Token,
) {
    return ApiRequest(
        `/summary/${KnowledgeItemId}`,
        {
            Method: "POST",
            Token,
        },
    );
}