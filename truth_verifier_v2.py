# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *
import json

class TruthVerifier(gl.Contract):
    def __init__(self):
        pass

    @gl.public.view
    def verify_claim(self, claim: str, source_url: str) -> str:
        # This is the non-deterministic block
        def evaluate() -> dict:
            # Fetch web page using gl.nondet.web.render
            page = gl.nondet.web.render(source_url, mode="html")
            excerpt = str(page)[:20000]

            prompt = f"""
            You are an unbiased fact-checker.
            CLAIM: <claim>{claim}</claim>
            SOURCE: <source>{excerpt}</source>
            Verify the claim using ONLY the source.
            Respond in JSON: {{"verdict": "True/False/Uncertain", "explanation": "..."}}
            """
            # Call LLM using gl.nondet.exec_prompt
            out = gl.nondet.exec_prompt(prompt, response_format="json")
            return out

        # This is the validation block (Equivalence Principle)
        def validate(leader_result) -> bool:
            own = evaluate()
            return leader_result["verdict"] == own["verdict"]

        # Run the non-deterministic block and wait for consensus
        result = gl.vm.run_nondet_unsafe(evaluate, validate)
        return json.dumps(result)
