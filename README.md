# *Exploring Pedagogical Applications of Large Language Models in English Literature Education*

A senior project conducted in partial fulfillment of a B.S. in Computer Science from Yale University. Focused on LLMs, RAG, and English literature pedagogy.

## Background

### Domain Background

Large language models – also known as LLMs – have revolutionized the world in a relatively short period. LLMs are composed of transformer networks that learn “context” and “meaning” during their analysis of sequential relationships in input data (4). Popular LLMs, such as GPT-3, have been integrated into consumer-facing web applications that have generated public engagement with AI.

While these consumer applications have broadly been used in personal and professional settings, they may be additionally suitable in an educational context. Advancements in technology have long had impacts on pedagogy. For example, the release of Khan Academy began a chapter of globalized self-learning powered by the Internet. LLM-integrated software applications can contribute to even more personalized learning experiences, where a student can interface with a virtual instructor using a method best suited to that student’s pedagogical profile.

### Project Background

This senior project is interested in how LLMs can be fine-tuned with retrieval-augmented generation (RAG) and integrated into software applications to enhance English literature education at the undergraduate level. To view a more detailed project plan, visit the proposal document [here](https://docs.google.com/document/d/14rrWWusI7MY39nANhZx1RwuvegR9GHVG4u8UIckODcw/edit?usp=sharing).

On the backend, this project uses:

-  `GPT-3`, OpenAI's 3rd-generation LLM

-  `langchain`, a framework that helps software engineers develop applications with LLMs

-  `ChromaDB`, an open-source embedding database

-  `beautifulsoup4`, a web-scraping package to process and transform raw data from course materials

## Ethics Statement on AI Pedagogy Approaches

While LLMs offer the potential for a more productive pedagogical experience, it may not be wise to fully replace the human student-instructor dynamic. AI assistants may democratize study for those who cannot access high-quality academic spaces. Additionally, AI assistants can be used as a supplemental tool to in-person learning. But dialogue between human students and human teachers should not be something to replace entirely. Rather, AI should focus on enhancing, rather than replacing, a person’s relationship with their learning.

## Source Code

This repository contains a few folders that correspond to the main deliverables of the project:

1.  `UX-Research-Report`: Contains a PDF of the submitted UX research report. Includes a brief literature survey on the nexus of LLMs and pedagogy, as well as the results from a research survey.

2.  `Retrieval-Augmented-Generation`: Contains preliminary data processing as well as the implementation of RAG with `langchain`, OpenAI's `gpt`, and a ChromaDB vector database.

3. `Class-Materials`: Contains assignments completed for the CPSC 490 course, including: project proposal, presentation slides, and reports.

### Installation Instructions

Follow these steps to access the Streamlit demo application and interface with the RAG-integrated model:
  
1. Clone the repository locally.

2. [Optional] Create a virtual environment with your package of choice.

3. Install the necessary packages in `requirements.txt` using `pip` with the `-r` flag.

4. Create a `.env` file and include a field with your OpenAI developer API key (use `OPENAI_API_KEY=YOURKEYHERE`).

5.  `cd` into the `Retrieval-Augmented-Generation` directory and run `streamlit run streamlit_app.py`.

6. Pull up `http://localhost:8501/` and (for better results) select which course you would like to discuss. Then, begin your session! (Note: The conversation is not persistent and will disappear when you refresh the page).


## References

1. Ahuja, A.S., et al. “ChatGPT for Good? On Opportunities and Challenges of Large Language Models for Education.” Learning and Individual Differences, 9 Mar. 2023, www.sciencedirect.com/science/article/abs/pii/S1041608023000195.

2. Jeon, J., Lee, S. Large language models in education: A focus on the complementary relationship between human teachers and ChatGPT. Educ Inf Technol 28, 15873–15892 (2023). https://doi.org/10.1007/s10639-023-11834-1

3. Lan, Yu-Ju, and Nian-Shing Chen. “Teachers’ Agency in the Era of LLM and Generative AI: Designing Pedagogical AI Agents.” Educational Technology & Society, vol. 27, no. 1, 2024, p. I–XVIII. JSTOR, https://www.jstor.org/stable/48754837. Accessed 25 Feb. 2024.

4. “What Are Large Language Models?” NVIDIA, www.nvidia.com/en-us/glossary/large-language-models/. Accessed 29 Jan. 2024.