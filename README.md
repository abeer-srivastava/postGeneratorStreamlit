

# Project: GenAI Post Generator

This tool is designed to help LinkedIn influencers generate new posts by learning from their past content. By analyzing previous posts, it identifies key characteristics such as topics, language, tone, and length—enabling future posts to align seamlessly with the influencer’s unique writing style.


### Example Use Case

Meet Mohan, a LinkedIn influencer who wants to maintain consistency in his content. Mohan uploads his previous posts into this tool. It analyzes them to extract recurring topics, tone, and style. Later, Mohan can simply select a topic, preferred post length, and language. With one click on **Generate**, the tool creates a brand-new post that mirrors his original voice.

---

## 🧠 Technical Architecture
1. **Stage 1: Post Analysis**

   * Past LinkedIn posts are collected and analyzed to extract metadata such as topic, language, tone, and length.

2. **Stage 2: Content Generation**

   * Based on selected attributes (topic, length, language), the tool uses few-shot learning. It references past similar posts to guide the LLM in replicating the user’s writing style.

---

## ⚙️ Getting Started

1. **Get an API Key**

   * Visit [Groq Console](https://console.groq.com/keys) to generate your API key.
   * Add the key to your `.env` file as follows:

     ```env
     GROQ_API_KEY=your_api_key_here
     ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**

   ```bash
   streamlit run main.py
   ```

---

## 📜 License & Terms

This software is licensed under the **MIT License**.

> ⚠️ **Important**: Commercial use is strictly **prohibited** without prior **written consent** from the author. Proper **attribution** is required in all copies or significant portions of the codebase.

---

**© Codebasics Inc. All rights reserved.**
