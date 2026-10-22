# GenLayer Truth Verifier

## 📌 Overview
The **Truth Verifier** is an Intelligent Contract built on GenLayer. It demonstrates how to combine live web data and AI to verify factual claims on-chain. 

Anyone can submit a claim (e.g., "The Eiffel Tower is 330 meters tall") and a trusted source URL. The contract fetches the live webpage, extracts the text, and uses an LLM to determine if the claim is **True**, **False**, or **Uncertain** based *strictly* on the provided source.

## 📍 Deployed Contract Address (GenLayer DevNet)
**`0x60c81D582ab50Bb899CF9aebCC20B84051C879EB`**

## ⚙️ How It Works (GenLayer Tech)
This contract showcases core GenLayer features:
*   **Web Access:** Uses `gl.nondet.web.render` to fetch the live HTML from the provided source URL.
*   **AI Evaluation:** Uses `gl.nondet.exec_prompt` to pass the web text and the claim to the AI, forcing it to respond in a structured JSON format.
*   **Optimistic Democracy:** Uses `gl.vm.run_nondet_unsafe` to achieve consensus. The validators check the leader's verdict against their own, ensuring the AI didn't hallucinate the fact-check.

## 🚀 How to Test
1. Open [GenLayer Studio](https://studio.genlayer.com).
2. Deploy the `truth_verifier.py` contract.
3. Call the `verify_claim` function with two arguments:
   *   **claim:** `"The first man to walk on the moon was Neil Armstrong."`
   *   **source_url:** `"https://en.wikipedia.org/wiki/Neil_Armstrong"`
4. The contract will return a JSON response with the verdict and explanation.

## 🧑‍💻 Built By
*   **ZestySam** 
*   Submitted as an accepted Builder contribution for the GenLayer ecosystem.
