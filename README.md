
# 🤖 Autogen_Blog_Maker (AutoGen + Ollama)

A **fully local, free-to-run multi-agent blog generation system** powered by  
[AutoGen 0.7+](https://github.com/microsoft/autogen) and [Ollama](https://ollama.ai).

This project lets multiple AI agents collaborate to automatically research, write, review,  
and save high-quality blog posts — all in Markdown format and all **completely offline**.

---

## 🚀 Features
- 🧠 Multi-agent system (Researcher, Writer, Reviewer)
- 🌐 Live web research (via DuckDuckGo)
- 📝 Auto-generates Markdown (`.md`) blog files
- 💬 Natural, structured writing
- ⚙️ Runs 100% locally with Ollama — no paid API keys
- 🧩 Works with models like **Mistral**, **Llama**, **Qwen**, **Gemma**, etc.

---

## 🧩 Installation

### 1️⃣ Install Ollama
Download and install **Ollama** from:  
👉 [https://ollama.ai/download](https://ollama.ai/download)

Then pull your preferred model (e.g., Mistral):
```bash
ollama pull mistral:latest
````

Start the Ollama server:

```bash
ollama serve
```

---

### 2️⃣ Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate     # macOS/Linux
.venv\Scripts\activate        # Windows
```

---

### 3️⃣ Install Dependencies

Install all required packages:

```bash
pip install duckduckgo-search autogen-agentchat autogen-ext[ollama]
```

> 💡 **Recommended versions:**
>
> ```bash
> pip install autogen-agentchat==0.7.5 autogen-ext==0.1.0 duckduckgo-search
> ```

---

## 🧠 Usage

### 1️⃣ Save the script

Save your Python script as **`blog_generator_autogen.py`**.

### 2️⃣ Run it

```bash
python blog_generator_autogen.py
```

### 3️⃣ Output

When complete, your generated blog will appear in:

```
blog_output/
 ┗ The_Future_of_AI_in_Healthcare.md
```

---

## ⚙️ Configuration

Edit topics and model directly inside `blog_generator_autogen.py`:

```python
topics = [
    "The Future of AI in Healthcare",
    "Sustainable Energy Solutions for 2025",
    "The Rise of Quantum Computing"
]

model = "mistral:latest"
```

You can also try other Ollama models like:

* `"llama3.2:latest"`
* `"gemma2:2b"`
* `"qwen2.5:3b"`

---

## 📂 Project Structure

```
📦 Autogen-Blog-Maker/
 ┣ 📜 blog_generator_autogen.py
 ┣ 📜 README.md
 ┗ 📁 blog_output/
    ┗ 📄 The_Future_of_AI_in_Healthcare.md
```

---

## 🧱 How It Works

| Agent          | Description                                   | Tools                 |
| :------------- | :-------------------------------------------- | :-------------------- |
| **Researcher** | Searches the web and compiles factual content | `web_search()`        |
| **Writer**     | Converts research into a polished blog post   | —                     |
| **Reviewer**   | Edits and saves the final markdown blog       | `save_blog_to_file()` |

Agents take turns using a **Round Robin Group Chat** managed by AutoGen.

---

## 💡 Example Output

Example file: `blog_output/The_Future_of_AI_in_Healthcare.md`

```markdown
# The Future of AI in Healthcare

Artificial Intelligence (AI) is transforming healthcare through automation,
predictive analytics, and personalized medicine.

## Key Applications
- Early diagnosis and disease prediction
- Robotic surgery and virtual health assistants
- AI-driven drug discovery

## Challenges Ahead
Ethical use, data privacy, and interpretability remain key concerns.

## Conclusion
AI is set to redefine healthcare delivery — making it more proactive, precise, and patient-centric.
```

---

## 🧰 Troubleshooting

| Issue                              | Solution                                                |
| :--------------------------------- | :------------------------------------------------------ |
| ❌ `ollama not found`               | Install and start Ollama (`ollama serve`)               |
| ❌ `duckduckgo_search` import error | `pip install duckduckgo-search`                         |
| ❌ No `.md` file saved              | Ensure `Reviewer` includes `save_blog_to_file` in tools |
| 🐢 Too slow?                       | Try smaller models like `gemma2:2b`                     |

---

## 🧑‍💻 Author

Built for developers exploring **Agentic AI**, **local LLM orchestration**, and **autonomous content generation**.

---

## 🪶 License

This project is licensed under the **Mozilla Public License 2.0 (MPL-2.0)**.
You may freely use, modify, and distribute this software under MPL terms.
See the [LICENSE](./LICENSE) for full details.

