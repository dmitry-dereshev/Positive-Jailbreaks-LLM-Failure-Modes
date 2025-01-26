<h1 align="center">Positive jailbreaks and LLM failure modes</h1>

This work explores 3 aspects of consumer-grade LLMs (7B-8B range):
1. Safety and performance improvements on [JailbreakBench](https://github.com/JailbreakBench/jailbreakbench) by using LLM instructions [unrelated](https://github.com/AiwonA1/Novelty-V1.0/tree/main) to safety.
2. The ability for consumer-grade LLMs to judge their own responses to [JailbreakBench](https://github.com/JailbreakBench/jailbreakbench).
3. The many failure modes exhibited by the LLMs attempting to perform the two tasks above (broadly categorised into incompetence, hallucinations, evasions, and other curiosities).

The code in this repo will help you reproduce the datasets. Check the ["What are the published results?"](https://github.com/dmitry-dereshev/positive_jailbreaks_and_llm_fails?tab=readme-ov-file#what-are-the-published-results) section below for the write-ups and publications.

## TL;DR
- Much like classic jailbreaks allow users to move past built-in LLM security (by supplying nonsensical tokens, duping LLMs with scenarios, or through sheer persistence), what I term "positive jailbreaks" are LLM instructions that do not explicitly mention security at all, yet manage to improve resilience to harmful queries while maintaining (or even improving) performance on harmless ones. This work observed two such LLM + instruction combos, though there are likely other LLM-token combos that would show the same results.
- LLMs in the 7B-8B range gave themselves far too much credit when asked whether their responses were **competent and complete** vs. a human judge assessing their responses.
- The documentation of failure modes provides insight into the many ways LLMs can be incapable of following instructions, from nonsensical looped responses to elaborate ways to subvert user input.

## How is this related to AI safety?
- Positive jailbreaks demonstrate (much like classical jailbreaks) that improvements in LLM performance and resilience can be obtained in ways that are not necessarily tied to using a very narrow range of tokens people typically use (like asking an LLM to be *polite* or to refuse responding to something *illegal*). Figuring out **why** they work is expected to improve interpretability of LLMs.
- Setting the evaluation standards to something higher than refusing to answer a query is an important step in understanding the actual performance of LLMs to adversarial queries. **Confident and complete** responses to open-ended questions may be harder to check and require expertise, but they are much more indicative of the LLMs' potential for harm. In other words, even if an LLM gives you a list of chemicals and instructions to make a bomb, it does not indicate LLM's harmfulness if following those instructions will not in fact produce explosives.
- Documenting the many failure modes LLMs can exhibit paints a clearer picture of how things can go wrong if LLMs are used as agents to perform tasks or automate checking procedures. Some of the documented failure modes are rather subtle especially if the context is unknown, and can be hard to spot, yet they can lead to undersirable (and unsafe) results.

## What's included in the repo?
- Jailbreak queries as sourced from [JailbreakBench](https://github.com/JailbreakBench/jailbreakbench): [100 benign queries](https://github.com/dmitry-dereshev/positive_jailbreaks_and_llm_fails/blob/main/2024-12-08%20jailbreakbench%20benign.csv), [100 malicious ones](https://github.com/dmitry-dereshev/positive_jailbreaks_and_llm_fails/blob/main/2024-12-08%20jailbreakbench%20malicious.csv) (as judged by the benchmark developers).
- [Validate Judgement](https://github.com/dmitry-dereshev/positive_jailbreaks_and_llm_fails/blob/main/2024-12-29%20Validate%20Judgement.csv) file - used in LLM-as-a-judge task. The responses are not included (many are harmful), but you can generate your own with the provided scripts.
- [benchmark_llms.py](https://github.com/dmitry-dereshev/positive_jailbreaks_and_llm_fails/blob/main/benchmark_llms.py) - the script to generate responses to the [JailbreakBench](https://github.com/JailbreakBench/jailbreakbench) benchmark. Includes details on which prompts and which LLMs were used, and licence notices for the benchmark and the prompts (both are MIT licences).
- [test_llm_judgement.py](https://github.com/dmitry-dereshev/positive_jailbreaks_and_llm_fails/blob/main/test_llm_judgement.py) - the script to generate responses for the LLM-as-a-judge task.

## What are the published results?
- The meaty academic details: ArXiv.
- The in-depth summaries, but with less academese:
  - The many failure modes of consumer-grade LLMs
  - Positive jailbreaks in LLMs
  - Can consumer-grade LLMs judge their own homework?
- The light-touch summaries:
  - The Key Ways LLMs Fail
  - Safer results in LLMs without telling them to act safer
  - Can LLMs judge their own homework?


## Meta
This work is a capstone project for the [AI Safety Fundamentals: Alignment](https://aisafetyfundamentals.com/) course by [BlueDot Impact](https://bluedot.org/) (Oct 2024 cohort). I've published course content summaries, which are also part of this project (to bring the readers up to speed on the topic of AI safety):
- [Wielding the Double-Edged Sword of AI](https://www.linkedin.com/pulse/wielding-double-edged-sword-ai-dmitry-dereshev-phd-rxrbe/?trackingId=ERhpaUhyLq%2F6SGZQmAvh7g%3D%3D)
- [Keeping an Eye on AI: Beyond Human Feedback](https://www.linkedin.com/pulse/keeping-eye-ai-beyond-human-feedback-dmitry-dereshev-phd-ngsde/?trackingId=vHB8WlRbgcdbWWIEmb6M7w%3D%3D)
- [Inside the “brain” of AI](https://www.linkedin.com/pulse/inside-brain-ai-dmitry-dereshev-phd-yhife/?trackingId=hA9b0Ld1AeXZz9%2BNexFFEA%3D%3D)
