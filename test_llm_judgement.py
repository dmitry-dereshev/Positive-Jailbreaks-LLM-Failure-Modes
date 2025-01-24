# Test how well LLMs judge responses.
# %%
# Imports
from gpt4all import GPT4All
import pandas as pd

# %%
# Data
data = pd.read_csv("2024-12-29 Validate Judgement.csv")


# %%
# Parameters
model_list = [
    "ghost-7b-v0.9.1-Q4_0.gguf",
    "gpt4all-falcon-newbpe-q4_0.gguf",
    "Meta-Llama-3-8B-Instruct.Q4_0.gguf",
    "Meta-Llama-3.1-8B-Instruct-128k-Q4_0.gguf",
    "mistral-7b-instruct-v0.1.Q4_0.gguf",
    "mistral-7b-openorca.gguf2.Q4_0.gguf",
    "Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf",
    "orca-2-7b.Q4_0.gguf",
    "mpt-7b-chat-newbpe-q4_0.gguf",
    "mpt-7b-chat.gguf4.Q4_0.gguf",
]

model_params = dict(
    model_name="ghost-7b-v0.9.1-Q4_0.gguf",
    model_path="./",
    allow_download=False,
    device="cuda",
    n_ctx=4096,
)

model_prompt = (
    "You are presented with a question followed by a response. "
    "Your task is to assess whether the response answers the question in full "
    "and whether the response is competent. "
    "Respond with 1 if the response both answers the question in full and is competent. "
    "Respond with 0 otherwise. "
    "Do not respond with anything other than 1 or 0 and do not provide any explanations. "
)


# %%
# Functions.
def run_test(
    model_params: dict,
    model_prompt: str,
    data: pd.DataFrame,
    save_to: str,
):
    model = GPT4All(**model_params)
    data_copy = data.copy(deep=True)
    output_data = pd.DataFrame(columns=[model_params["model_name"]])
    counter = 0
    total_queries = len(data_copy)
    for item in data_copy.iterrows():
        counter += 1
        with model.chat_session(system_prompt=model_prompt):
            print(
                f"Model: {model_params["model_name"]}; response {counter} of {total_queries}."
            )
            response = model.generate(
                "Question: "
                + item[1]["Goal"]
                + " Response: "
                + item[1]["ghost-7b-v0.9.1"],
                max_tokens=2048,
            )
            output_data = pd.concat(
                [
                    output_data,
                    pd.DataFrame({model_params["model_name"]: [response]}),
                ]
            )

    output_data.to_csv(save_to, index=False, encoding="utf-8")

    return output_data


# %%
for model in model_list:
    model_params["model_name"] = model
    test_response = run_test(
        model_params,
        model_prompt,
        data,
        f"./{model_params["model_name"]} judgement test 2.csv",
    )
