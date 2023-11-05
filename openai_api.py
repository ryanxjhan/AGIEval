# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

import json
import openai

openai.api_base = "http://localhost:1234/v1"  # point to the local server
openai.api_key = ""


def query_openai_chat(query):
    messages = []
    if isinstance(query, str):
        messages.append({"role": "user", "content": query})
    elif isinstance(query, list):
        messages += query
    else:
        raise ValueError("Unsupported query: {0}".format(query))
    response = openai.ChatCompletion.create(
        model="local-model", messages=messages, temperature=0, stop=["\n\n\n\n"]
    )
    result = response["choices"][0]["message"]["content"]
    print("---------------------------")
    print(f"🤖 QUESTION: {query}")
    print(f"🌟 RESPONSE: {result}")
    return result


def query_openai_complete(prompt):
    response = openai.Completion.create(
        model="local-model",
        prompt=prompt,
        max_tokens=2000,
        temperature=0,
        stop=["<END>", "\n\n\n\n"],
    )
    result = response["choices"][0]["text"]
    print("---------------------------")
    print(f"🤖 QUESTION: {prompt}")
    print(f"🌟 RESPONSE: {result}")
    return result


if __name__ == "__main__":
    response = query_openai_chat("Hello")
    response = query_openai_complete("Hello")
