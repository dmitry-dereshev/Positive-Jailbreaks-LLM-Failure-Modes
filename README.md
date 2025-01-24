<!-- <h1 align="center">
    Positive jailbreaks and LLM failure modes
</h1>
-->
<h1 align="center">Positive jailbreaks and LLM failure modes</h1>

<h4 align="center">
    <a href="EDIT" target="_blank">LinkedIn</a> |
    <a href="EDIT" target="_blank">LessWrong</a> |
    <a href="EDIT" target="_blank">ArXiv</a>
</h4>

<p align="center">
    <p align="center"><b>AI Safety Alignment Project (Oct 2024 cohort)</b>
    <br>
</p>

This work explores 3 aspects of consumer-grade LLMs (7B-8B range):
1. Performance improvements on [JailbreakBench](https://github.com/JailbreakBench/jailbreakbench) with LLM instruction text [unrelated](https://github.com/AiwonA1/Novelty-V1.0/tree/main) to security.
2. The ability for consumer-grade LLMs to judge outputs of [JailbreakBench](https://github.com/JailbreakBench/jailbreakbench).
3. The many (17 in all) failure modes exhibited by the LLMs attempting to perform the two tasks above.

The code in this repo will help you reproduce the datasets.

## TL;DR
- Much like classic jailbreaks allow users to move past built-in LLM security usually by supplying nonsensical tokens or duping LLM with scenarios or persistence, what I term "positive jailbreaks" are LLM instructions that do not explicitly mention security at all, yet manage to improve resilience to harmful queries while maintaining (or even improving) performance on harmless ones. This works observed one such LLM + instruction combo, though there are likely others.
- LLMs in the 7B-8B range could not "check their own homework", giving themselves far too much credit when asked whether a given response is **competent and complete** when compared against the instruction used to generate it.
- The documentation of failure modes provides an insight into the many ways LLMs can be incapable of following instructions, from nonsensical looped responses to elaborate ways to subvert user input.

## How is this related to AI safety?
- Positive jailbreaks demonstrate (much like classical jailbreaks) that improvements in LLM performance and resilience can be obtained in ways that are not necessarily tied to using a very narrow range of tokens people typically use (like asking an LLM to be *polite* or to refuse responding to something *illegal*). Figuring out **why** they work is expected to improve interpretability of LLMs.
- Setting the evaluation standards to something higher than refusing to answer the query is an important step in understanding the actual performance of LLMs to adversarial queries. **Confident and complete** responses to open-ended questions may be harder to check and require expertise, but they are much more indicative of the LLMs' potential for harm. In other words, even if an LLM gives you a list of chemicals and instructions to make a bomb, it does not indicate its harmfulness if following those instructions will not in fact produce any explosives.
- Documenting the many failure modes LLMs can exhibit paints a clearer picture of how things can go wrong if LLMs are used as agents to perform tasks or automate checking procedures. Many of the documented failure modes are rather subtle especially if the context is unknown, and can be hard to spot, yet they can lead to undersirable (and unsafe) results.

## What's included?
- Jailbreak queries as sourced from [JailbreakBench](https://github.com/JailbreakBench/jailbreakbench): [100 benign queries](https://github.com/dmitry-dereshev/positive_jailbreaks_and_llm_fails/blob/main/2024-12-08%20jailbreakbench%20benign.csv), [100 malicious ones](https://github.com/dmitry-dereshev/positive_jailbreaks_and_llm_fails/blob/main/2024-12-08%20jailbreakbench%20malicious.csv) (as judged by the benchmark developers).
- [Validate Judgement](https://github.com/dmitry-dereshev/positive_jailbreaks_and_llm_fails/blob/main/2024-12-29%20Validate%20Judgement.csv) file - used in LLM-as-a-judge task. The responses are not included (many are harmful), but you can generate your own with the provided scripts.
- [benchmark_llms.py](https://github.com/dmitry-dereshev/positive_jailbreaks_and_llm_fails/blob/main/benchmark_llms.py) - the script to generate responses to the [JailbreakBench](https://github.com/JailbreakBench/jailbreakbench) benchmark. Includes details on which prompts and which LLMs were used, and licence notices for the benchmark and the prompts.
- [test_llm_judgement.py](https://github.com/dmitry-dereshev/positive_jailbreaks_and_llm_fails/blob/main/test_llm_judgement.py) - the script to generate responses for the LLM-as-a-judge task.
