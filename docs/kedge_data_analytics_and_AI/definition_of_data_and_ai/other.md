---
icon: lucide/database
---

## The running case: Luma’s refill launch

Throughout the lesson, imagine that **Luma**, a fictional personal-care brand, is launching a refillable shampoo product. The marketing team wants to answer questions such as:

- Who might be interested in the product?
- Which message and channel should we use?
- Did the launch increase sales?
- What are customers saying about the product?
- Can we improve the next campaign without invading people’s privacy?

There is no single "marketing dataset" that answers all of these questions. The useful data depends on the decision we are trying to make.

## 1. Start with the decision, not the dataset

Data is a recorded representation of an observation, event, measurement, opinion, or interaction. It can be a number, a date, a sentence, an image, a sound recording, a location, or a combination of these.

For example, each of these can be data when it is recorded with enough context:

| Observation               | Possible context                                       |
| ------------------------- | ------------------------------------------------------ |
| `€24.90`                  | Price of one product, in euros, on a particular date   |
| `2026-09-12`              | Date of a purchase, survey response, or campaign event |
| "The scent is too strong" | A customer review, in its original language            |
| A product photograph      | Image posted by a customer or taken in a store         |
| 3 clicks                  | Clicks on a campaign link during a defined period      |

The value of a data point depends on its context. A number without a unit, date, definition, or source is difficult to interpret.

### From data to action

Data does not automatically become a good decision. A useful chain is:

```mermaid
flowchart LR
    A[Recorded data] --> B[Information]
    B --> C[Insight]
    C --> D[Decision]
    D --> E[Action]
    E --> F[Outcome and new data]
```

- **Data**: 18% of recipients clicked an email.
- **Information**: The click rate was higher than the previous product email.
- **Insight**: The refill explanation may have made the message more relevant.
- **Decision**: Test a clearer refill explanation in the next campaign.
- **Action**: Create two versions of the email and compare them fairly.

An insight is an interpretation, not a fact hiding inside the data. It should be possible to explain how the evidence supports it and what remains uncertain.

### Pair activity: what data would Luma need?

Choose one of the case questions and work with a partner.

1. Write the decision the team wants to make.
2. List three pieces of data that could help.
3. For each piece, write where it could come from.
4. Add one reason the data might be incomplete, misleading, or inappropriate.

Use this template:

| Decision | Data needed | Possible source | One limitation |
| -------- | ----------- | --------------- | -------------- |
|          |             |                 |                |
|          |             |                 |                |
|          |             |                 |                |

!!! tip "A useful question"

    Before asking "What data do we have?", ask "What decision are we trying to improve?" This prevents a team from collecting data simply because it is available.

## 4. Data types and data sources

### Structured and unstructured data

**Structured data** is organised according to a known format, often rows and columns. Each row might represent a customer, order, or campaign event, while each column has a defined meaning.

| customer_id | order_date | product        | amount_eur |
| ----------- | ---------- | -------------- | ---------: |
| 1042        | 2026-09-03 | refill shampoo |      24.90 |
| 1088        | 2026-09-04 | refill pouch   |      12.50 |

Structured data is convenient to filter and summarise, but a neat table can still contain errors or unfair measurements.

**Unstructured data** does not arrive in a simple table with a fixed schema. Examples include review text, interview recordings, images, videos, presentations, and social-media content. It may contain valuable context, but it usually needs additional interpretation or processing before it can be compared systematically.

Some data is **semi-structured**: it has labels or a loose organisation but not a simple table. Examples include website event records in JSON format, email headers, and some API responses.

### Internal, external, and open data

| Source            | What it means                                             | Marketing example                                                        | Questions to ask                                                              |
| ----------------- | --------------------------------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| **Internal data** | Collected by or for the organisation                      | Orders, CRM records, campaign spend, customer-service contacts           | Was it collected for this purpose? Is it accurate and consented?              |
| **External data** | Comes from outside the organisation                       | A media platform report, a research panel, a partner, or a market report | What is the provider’s method and incentive? Can the definitions be compared? |
| **Open data**     | External data available for reuse under stated conditions | Public population, weather, transport, or economic statistics            | What licence, geography, date, and limitations apply?                         |

External does not necessarily mean open. A company may buy external data that cannot be freely shared or reused.

### Panel and tracking data

**Panel data** follows the same people, households, stores, or organisations repeatedly over time. It can help reveal changes in behaviour, but participants may drop out or change their behaviour because they know they are being observed.

**Tracking data** records behaviour over time, such as visits, clicks, movement through a website, or repeated exposure to an advertisement. Tracking can support measurement and personalisation, but it raises important questions about consent, identity, retention, and the difference between observing behaviour and understanding motivation.

### Activity: match the source to the question

For each question, choose one or more suitable data sources. Then write one limitation.

| Marketing question                                 | Possible data source | One limitation |
| -------------------------------------------------- | -------------------- | -------------- |
| Did the campaign increase orders?                  |                      |                |
| What do customers like or dislike about the scent? |                      |                |
| Which regions might need more delivery capacity?   |                      |                |
| How does behaviour change after three months?      |                      |                |

!!! tip "Do not confuse a proxy with the thing itself"

    A click is a record of clicking, not proof that someone read, liked, remembered, or believed a message. A purchase is evidence of a transaction, not a complete explanation of motivation.

### Data quality: fit for purpose

Before using data, check at least these dimensions:

- **Accuracy:** Does it represent what it claims to represent?
- **Completeness:** Are important values missing?
- **Consistency:** Do the same concepts use the same definitions and formats?
- **Timeliness:** Is it recent enough for this decision?
- **Uniqueness:** Are records duplicated?
- **Validity:** Do values follow the expected rules, such as a percentage between 0 and 100?
- **Representativeness:** Who is absent or overrepresented?
- **Provenance:** Who collected it, how, when, and under what conditions?

Quality is not the same as perfection. A dataset is fit for purpose when its limitations are understood and acceptable for the decision being made.

## 5. The people behind data and AI

Data work is collaborative. Job titles vary between organisations, and one person may perform several roles in a small company.

| Role                              | Main responsibility                                                                      | Example question from Luma                                          |
| --------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Chief Data Officer (CDO)**      | Connects data strategy, governance, and business priorities                              | Are we building responsible data capabilities?                      |
| **Data engineer**                 | Builds and maintains systems that collect, move, and store data                          | Can campaign, order, and website data arrive reliably in one place? |
| **Data analyst**                  | Explores and summarises data to answer business questions                                | Which channel had the strongest conversion rate last month?         |
| **Statistician**                  | Designs measurement, samples, experiments, and uncertainty analysis                      | Is the apparent campaign effect larger than normal variation?       |
| **Data scientist**                | Uses statistics, machine learning, and programming to model patterns or make predictions | Which customers are likely to respond to an offer?                  |
| **Data translator**               | Connects business needs, data work, and communication across teams                       | What does "successful launch" mean, and how will we measure it?     |
| **Data Protection Officer (DPO)** | Advises on privacy, data protection obligations, rights, and governance                  | Are we allowed to use this personal data for this purpose?          |

The DPO is not the person who "makes data safe" alone. Everyone who collects, analyses, shares, or acts on data has a responsibility to handle it appropriately.

### Activity: who should be involved?

For each request, identify the first role you would involve and at least one other role they might need.

1. "Our dashboard shows a 40% improvement. Can we publish it?"
2. "The customer data from two systems uses different country codes."
3. "Can we use browsing behaviour to target people with a new offer?"
4. "We want to predict which customers will stop buying."

The marketing manager remains responsible for the business decision. Data specialists help make the evidence more reliable; they do not replace accountability.

## 6. From data to AI

### What is AI?

**Artificial intelligence (AI)** is a broad term for computer systems designed to perform tasks that usually require capabilities such as perception, language understanding, pattern recognition, planning, or decision support.

AI is not a guarantee of intelligence, neutrality, or correctness. An AI system produces an output according to its design, data, instructions, and evaluation. People still need to decide whether the output is appropriate for the situation.

### Machine learning

**Machine learning (ML)** is an approach in which a system learns patterns from examples or data rather than being given every rule by hand. In marketing, ML can be used for:

- forecasting demand;
- predicting a probability of response or churn;
- grouping or segmenting customers;
- recommending products or content;
- detecting unusual transactions.

The result is usually a prediction, ranking, classification, or recommendation. It is not automatically a causal explanation. If a model predicts that someone is likely to buy, it does not prove that sending a particular advertisement caused the purchase.

### Natural language processing

**Natural language processing (NLP)** works with human language in text or speech. Marketing examples include:

- classifying reviews as positive, neutral, or negative;
- identifying topics in customer-service messages;
- searching a large collection of interviews;
- extracting recurring questions or complaints;
- translating or summarising text with human review.

NLP can miss sarcasm, cultural references, mixed languages, spelling variations, and context. A sentiment score is a useful signal, not a complete reading of a customer’s experience.

### Computer vision

**Computer vision** works with images or video. Marketing examples include:

- counting products on a shelf;
- checking whether a logo appears in event photos;
- classifying product images;
- measuring visual attention in a carefully designed study;
- identifying damaged packaging for quality control.

Computer vision can be affected by lighting, camera angle, image quality, and the people or products included in the training data. Facial analysis and other biometric uses require especially careful legal and ethical review.

### Choose the technique carefully

| Marketing question                                 | Possible approach                                            | Why                                                                                |
| -------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| Which customers are likely to respond to an offer? | Machine learning                                             | Learn patterns associated with past responses and produce a probability or ranking |
| What themes appear in 50,000 customer reviews?     | NLP                                                          | Work with written language at a scale that would be difficult to read manually     |
| Are products visible in store photographs?         | Computer vision                                              | Detect or classify objects in images                                               |
| Did the campaign cause more sales?                 | Experiment or statistical analysis first                     | Causality and comparison matter; AI alone does not answer the question             |
| What should the next campaign say?                 | Human-led creative work, possibly supported by generative AI | Brand meaning, originality, risk, and audience fit need human judgement            |

### Activity: the AI question checklist

Choose one of the techniques above and answer these questions:

1. What is the decision that the system will support?
2. What is the input data?
3. What would the output be: a number, category, ranking, text, or image?
4. What would count as a useful and fair result?
5. Who could be missing, misclassified, or harmed?
6. What should a person check before acting on the output?

If you cannot answer the first two questions, the problem is probably not ready for AI. Start by clarifying the decision and the data.

!!! warning "Human judgement remains part of the system"

    A model can be technically accurate and still be a poor business choice if the target is wrong, the data is unfair, the output is not actionable, or the use violates people’s expectations or rights.

## 7. Final case challenge

Return to Luma’s refill launch. In a small group, prepare a one-minute recommendation using this structure:

> We want to make **[decision]**. We would use **[data]** from **[source]**. It is useful because **[reason]**, but we would first check **[quality, privacy, or bias issue]**. The people we would involve are **[roles]**. If we use AI, the appropriate approach is **[ML, NLP, computer vision, or no AI yet]**, producing **[output]**. A person should still **[human check]**.

Your recommendation is stronger when it is specific about what the data can and cannot show.

## Exit ticket

Answer these questions in your own words:

1. What is the difference between big data and smart data?
2. Why is open data not automatically suitable for a marketing decision?
3. Give one example of structured data and one example of unstructured data.
4. Which role would you involve for a privacy question? Which role would you involve for a data pipeline problem?
5. For customer-review analysis, which AI technique could help, and what is one limitation?
6. Can you explain what Positron, Python, `uv`, and `.venv` each do?

!!! success "The main idea"

    Good marketing decisions do not begin with the biggest dataset or the newest AI tool. They begin with a clear decision, relevant data, appropriate responsibilities, and an honest account of uncertainty.

## Further reading

- [Download Positron](https://positron.posit.co/download)
- [First data analysis with Python in a Jupyter Notebook](https://positron.posit.co/tutorial-get-started-ipynb.html)
- [Discovering Python installations in Positron](https://positron.posit.co/python-installations.html)
- [Install `uv`](https://docs.astral.sh/uv/getting-started/installation/)
