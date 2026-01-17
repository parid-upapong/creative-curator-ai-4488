import os
import json
from typing import Dict, Any
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

class CreativeAnalysisAgent:
    """
    Agent responsible for analyzing creative portfolios and generating 
    standardized JSON-C reports and scores.
    """
    def __init__(self, api_key: str):
        self.llm = ChatOpenAI(
            model="gpt-4o",
            api_key=api_key,
            temperature=0.2
        )
        self.system_prompt = self._load_scoring_logic()

    def _load_scoring_logic(self) -> str:
        return """
        You are the 'Global Creative Standard AI'. 
        Your role is to analyze the provided creative work (images, text, or links) 
        and map them to the JSON-C schema.
        
        CRITERIA:
        1. Technical Proficiency: Look for alignment, hierarchy, and craftsmanship.
        2. Commercial Readiness: Is this work ready to be sold to a high-end client?
        3. Innovation: Does it push boundaries or follow a template?
        
        OUTPUT: You must return ONLY a valid JSON object following the JSON-C schema.
        """

    async def analyze_portfolio(self, assets: list, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Processes a list of assets and returns a scored JSON-C report.
        """
        prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("user", "Analyze these assets: {assets}. Context: {context}")
        ])
        
        chain = prompt | self.llm
        
        # In production, vision models would process image URLs here.
        # For this spec, we simulate the logic integration.
        response = await chain.ainvoke({
            "assets": json.dumps(assets),
            "context": json.dumps(context)
        })
        
        try:
            return json.loads(response.content)
        except json.JSONDecodeError:
            return {"error": "Failed to parse AI response into JSON-C"}

# Example Usage
# agent = CreativeAnalysisAgent(api_key="...")
# report = await agent.analyze_portfolio(["https://cdn.art.com/work1.jpg"], {"target_industry": "FinTech"})