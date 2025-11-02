import asyncio
import os
from duckduckgo_search import DDGS
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination, MaxMessageTermination
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient

async def web_search(query: str, max_results: int = 5) -> str:
    try:
        ddgs = DDGS()
        results = ddgs.text(query, max_results=max_results)
        if not results:
            return f"No results found for query: {query}"
        formatted = f"Web Search Results for '{query}':\n\n"
        for i, r in enumerate(results, 1):
            formatted += f"{i}. {r['title']}\n   URL: {r['href']}\n   Summary: {r['body']}\n\n"
        return formatted
    except Exception as e:
        return f"Error during web search: {str(e)}"

async def save_blog_to_file(filename: str, content: str) -> str:
    try:
        os.makedirs("blog_output", exist_ok=True)
        safe_name = filename.replace(" ", "_").replace("/", "_")
        if not safe_name.endswith(".md"):
            safe_name += ".md"
        path = os.path.join("blog_output", safe_name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"✅ Blog saved: {path}"
    except Exception as e:
        return f"❌ Error saving file: {str(e)}"

async def create_blog_with_agents(topic: str, ollama_model: str = "mistral:latest"):
    print(f"\n{'='*70}")
    print(f"🤖 Multi-Agent Blog Generation System (AutoGen + Ollama)")
    print(f"{'='*70}\nTopic: {topic}\nModel: {ollama_model}\n{'='*70}\n")

    model_client = OllamaChatCompletionClient(model=ollama_model)

    researcher = AssistantAgent(
        name="Researcher",
        description="Web research specialist",
        model_client=model_client,
        tools=[web_search],
        system_message="""You are a web research specialist.
1. Analyze the topic.
2. Generate 2-3 search queries.
3. Use the web_search tool.
4. Summarize findings into key points, data, and examples.
End with: RESEARCH_COMPLETE""",
    )

    writer = AssistantAgent(
        name="Writer",
        description="Expert blog writer",
        model_client=model_client,
        system_message="""You are an expert blog writer.
1. Use research to write an engaging markdown blog:
   - # Title
   - Intro
   - ## Sections
   - Conclusion
2. End with: DRAFT_COMPLETE""",
    )

    reviewer = AssistantAgent(
        name="Reviewer",
        description="Blog editor and reviewer",
        model_client=model_client,
        tools=[save_blog_to_file],
        system_message=f"""You are a blog editor.
1. Review the blog for clarity and flow.
2. Fix any grammar or structure issues.
3. Once finalized, call save_blog_to_file with:
   - filename="{topic}"
   - content=final_blog
4. End with: BLOG_SAVED - TERMINATE""",
    )

    termination = TextMentionTermination("TERMINATE") | MaxMessageTermination(30)
    team = RoundRobinGroupChat(participants=[researcher, writer, reviewer], termination_condition=termination)

    task = f"Create a detailed, high-quality blog about '{topic}'."
    result = await Console(team.run_stream(task=task), output_stats=True)

    print(f"\n{'='*70}\n✅ Blog Complete!\n📊 Messages: {len(result.messages)}\n🛑 Reason: {result.stop_reason}\n{'='*70}\n")
    return result

async def main():
    topics = ["The future of general artificial intelligence", "Advancements in renewable energy technologies"]
    model = "mistral:latest"
    for t in topics:
        try:
            await create_blog_with_agents(t, ollama_model=model)
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback; traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
