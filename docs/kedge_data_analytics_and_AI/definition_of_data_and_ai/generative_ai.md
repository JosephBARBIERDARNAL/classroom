---
icon: lucide/database
---

## Transformers

In 2017, Google researchers publish a now extremely famous paper named [Attention is all you need](https://papers.nips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf) presenting the **Transformer architecture**.

<iframe src="https://ig.ft.com/generative-ai/" width="100%" height="700"></iframe>

Source: [Generative AI exists because of the transformer](https://ig.ft.com/generative-ai/)

## An LLM isn't a database

It might feel natural to compare an LLM to a search tool like Google, but they are very different. An LLM is litteraly one (or multiple) files stored somewhere. It contains between **dozens of millions** (see example below) to **hundreds of billions** (Claude, ChatGPT, etc)

Here is an AI running completly "offline". Once it says _"Ready: ...."_, you can:

- turn off your wifi
- try to chat with it

!!! warning

      - Don't refresh the page, otherwise it won't work.
      - This might slowdown your computer a little bit, but there are no risks.

<iframe src="./local_llm.html" width="100%" height="600"></iframe>

> Everything you asked the AI here is 100% private, nobody, even myself, could ever know what you'll ask it.

As you make some tests, you'll see that:

- answers are kind of weird and not very clear
- it often stops mid-sentence

The latter is because, at each step when making predictions, computes **what is the next word in that sentence** (or token as we should say). Its reasonning is basically something like this:

- Given all tokens so far, it computes a **probability distribution over the possible next tokens**. In the sentence _=="I hope I'll have a good [...]"==_, the LLM tries to figure out what _=="[...]"==_ could be? It's likely to predict something like: 40% chance to be _=="day"==_, 30% change to be _=="morning"==_, etc.
- A **token is selected** from that distribution: could be the one with the highest chance (e.g., _=="day"==_) or some more sophisticated method.
- That token is **appended to the context**: the sentence becomes _=="I hope I'll have a good day [...]"==_.
- And the process **repeats**.
- Generation stops when the model produces a **special end-of-sequence (EOS) token**, or when some external stopping condition is reached (such as a maximum token limit).

## Before Gen AI

As we said before, there was "AI" long before "Generative AI", and non-generative AI still heavily exist today. The process is exactly the same:

- gather a lot of data. In practice it's often just users data.
- train an AI model on it with a specific task.
- evaluate that model
- make inference with it

The list could be much longer, but the following are the most common use cases:

=== "fraud detection"

      *Detects suspicious transactions or unusual behavior that may indicate fraud, such as stolen credit cards or unauthorized payments.*

=== "recommendation systems"

      *Predicts what content or products a user is most likely to be interested in based on their behavior, preferences, and similar users. This is used for example by youtube, tiktok, instagram, vinted, ...*

=== "medical image analysis"

      *Analyzes medical images such as X-rays, MRIs, or CT scans to help identify abnormalities, diseases, or other relevant patterns.*

=== "churn prediction"

      *Predicts which customers are likely to stop using a product or service, allowing companies to take action to retain them.*

Most of those usages fall into the **2 main categories**:

- regression: predict a number (e.g., how much ice creams we need at this store next week)
- classification: predict a category (e.g., does this patient has a tumor or not?) or a probability (e.g., what are the odd of this patient having a tumor?)

!!! question

      In your opinion, an LLM does regression or classification?

## Going further:

- [Video, FR] [Arthur Mensch, co-founder of Mistral AI, is being questioned at the National Assembly](https://www.youtube.com/watch?v=kKWOkWv6pJM)
- [Blog, EN] [Meet the $4 Billion AI Superstars That Google Lost](https://www.bloomberg.com/opinion/features/2023-07-13/ex-google-scientists-kickstarted-the-generative-ai-era-of-chatgpt-midjourney)
