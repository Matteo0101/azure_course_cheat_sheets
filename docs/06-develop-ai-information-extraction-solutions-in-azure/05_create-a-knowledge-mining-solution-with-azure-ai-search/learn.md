## What is Azure AI Search?

Azure AI Search provides a cloud-based solution for indexing and querying a wide range of data sources, and creating comprehensive and high-scale search solutions. It provides the infrastructure and tools to create search solutions that extract data from structured, semi-structured, and non-structured documents and other data sources.

With Azure AI Search, you can:

- Index documents and data from a range of sources.
- Use AI skills to enrich index data.
- Store extracted insights in a knowledge store for analysis and integration.

Azure AI Search indexes contain insights extracted from your data; which can include text inferred or read using OCR from images, entities and key phrases detection through text analytics, and other derived information based on AI skills that are integrated into the indexing process.

> Diagram of Azure AI Search supporting multiple applications.

Azure AI Search has many applications, including:

- Implementing an enterprise search solution to help employees or customers find information in websites or applications.
- Supporting retrieval augmented generation (RAG) in generative AI applications by using vector-based indexes for prompt grounding data.
- Creating knowledge mining solutions in which the indexing process is used to infer insights and extract granular data assets from documents to support data analytics.

In this module, we'll focus on Azure AI Search in knowledge mining scenarios.

## Extract data with an indexer

At the heart of Azure AI Search solutions is the creation of an index An index contains your searchable content and is created and updated, unsurprisingly, by an indexer.

The indexing process starts with a data source: the storage location of your original data artifacts; for example, an Azure blob store container full of documents, a database, or some other store.

The Indexer automates the extraction and indexing of data fields through an enrichment pipeline, in which it applies document cracking to extract the contents of the source documents and applies incremental steps to create a hierarchical (JSON-based) document with the required fields for the index definition.

The result is a populated index, which can be queried to return specified fields from documents that match the query criteria.

## How documents are constructed during indexing
The indexing process works by creating a document for each indexed entity. During indexing, an enrichment pipeline iteratively builds the documents that combine metadata from the data source with enriched fields extracted or generated by skills. You can think of each indexed document as a JSON structure, which initially consists of a document with the index fields you have mapped to fields extracted directly from the source data, like this:

- document
    - metadata_storage_name
    - metadata_author
    - content

When the documents in the data source contain images, you can configure the indexer to extract the image data and place each image in a normalized_images collection, like this:

- document
    - metadata_storage_name
    - metadata_author
    - content
    - normalized_images
    - image0
    - image1

Normalizing the image data in this way enables you to use the collection of images as an input for skills that extract information from image data.

Each skill adds fields to the document, so for example a skill that detects the language in which a document is written might store its output in a language field, like this:

- document
    - metadata_storage_name
    - metadata_author
    - content
    - normalized_images
    - image0
    - image1
    - language

The document is structured hierarchically, and the skills are applied to a specific context within the hierarchy, enabling you to run the skill for each item at a particular level of the document. For example, you could run an optical character recognition (OCR) skill for each image in the normalized images collection to extract any text they contain:

- document
    - metadata_storage_name
    - metadata_author
    - content
    - normalized_images
        - image0
            - Text
        - image1
            - Text
    - language

The output fields from each skill can be used as inputs for other skills later in the pipeline, which in turn store their outputs in the document structure. For example, we could use a merge skill to combine the original text content with the text extracted from each image to create a new merged_content field that contains all of the text in the document, including image text.

- document
    - metadata_storage_name
    - metadata_author
    - content
    - normalized_images
        - image0
            - Text
        - image1
            - Text
        - language
        - merged_content
The fields in the final document structure at the end of the pipeline are mapped to index fields by the indexer in one of two ways:

Fields extracted directly from the source data are all mapped to index fields. These mappings can be implicit (fields are automatically mapped to in fields with the same name in the index) or explicit (a mapping is defined to match a source field to an index field, often to rename the field to something more useful or to apply a function to the data value as it is mapped).
Output fields from the skills in the skillset are explicitly mapped from their hierarchical location in the output to the target field in the index.

## Enrich extracted data with AI skills

The enrichment pipeline that is orchestrated by an indexer uses a skillset of AI skills to create AI-enriched fields. The indexer applies each skill in order, refining the index document at each step.

## Built-in skills
Azure AI Search provides a collection of built-in skills that you can include in a skillset for your indexer. Built-in skills include functionality from Azure AI services such as Azure AI Vision and Azure AI Language, enabling you to apply enrichments such as:

- Detecting the language that text is written in.
- Detecting and extracting places, locations, and other entities in the text.
- Determining and extracting key phrases within a body of text.
- Translating text.
- Identifying and extracting (or removing) personally identifiable information (PII) within the text.
- Extracting text from images.
- Generating captions and tags to describe images.

To use the built-in skills, your indexer must have access to an Azure AI services resource. You can use a restricted Azure AI search resource that is included in Azure AI Search (and which is limited to indexing 20 or fewer documents) or you can attach an Azure AI services resource in your Azure subscription (which must be in the same region as your Azure AI Search resource).

## Custom skills
You can further extend the enrichment capabilities of your index by creating custom skills. As the name suggests, custom skills perform custom logic on input data from your index document to return new field values that can be incorporated into the index. Often, custom skills are "wrappers" around services that are specifically designed to extract data from documents. For example, you could implement a custom skill as an Azure Function, and use it to pass data from your index document to an Azure AI Document Intelligence model, which can extract fields from a form.

# 🔍 Search an Index with Azure AI Search

## 🧩 Problem  
You need to implement a search functionality that allows users to retrieve, filter, and sort information from a collection of documents.

## ☁️ Solution with Azure  
Use **Azure AI Search** to create and query a searchable index of JSON documents. Azure AI Search supports full-text search and structured queries using Lucene syntax.

## 🧱 Required Components  
- **Azure AI Search service**
- **Index** with defined fields and attributes:
  - `key`: Unique identifier for each document
  - `searchable`: Enables full-text search
  - `filterable`: Enables filtering
  - `sortable`: Enables sorting
  - `facetable`: Enables faceted navigation
  - `retrievable`: Determines if the field is returned in results

## 🏗️ Architecture / Development  
1. **Index Creation**: Define fields and attributes.
2. **Query Submission**: Client applications send queries using the Search API with parameters:
   - `search`: Query terms
   - `queryType`: `simple` or `full` Lucene syntax
   - `searchFields`: Fields to search
   - `select`: Fields to return
   - `searchMode`: `any` or `all` (e.g., match any or all terms)
3. **Query Processing Stages**:
   - **Parsing**: Build query tree (term, phrase, prefix queries)
   - **Lexical Analysis**: Normalize terms (lowercase, remove stopwords, stemming)
   - **Document Retrieval**: Match query terms with index
   - **Scoring**: Rank results using TF/IDF

## ✅ Best Practices / Considerations  
- Use `filterable` and `sortable` attributes to enable efficient result refinement.
- Choose `simple` syntax for basic queries and `full` for advanced filtering and expressions.
- Use `searchMode` to control result inclusiveness.
- Optimize index design based on expected query patterns.

## ❓ Sample Exam Questions  
1. **Which index field attribute allows a field to be used in full-text search?**  
   A. `filterable`  
   B. `searchable` ✅  
   C. `sortable`  
   D. `facetable`

2. **What is the purpose of the `searchMode` parameter in a query?**  
   A. To define the index schema  
   B. To specify the fields to return  
   C. To determine how multiple search terms are evaluated ✅  
   D. To enable sorting of results

3. **Which syntax should you use for complex queries with regular expressions?**  
   A. Simple  
   B. Full ✅  
   C. Basic  
   D. Advanced

## Filtering results
You can apply filters to queries in two ways:

- By including filter criteria in a simple search expression.
- By providing an OData filter expression as a $filter parameter with a full syntax search expression.

You can apply a filter to any filterable field in the index.

For example, suppose you want to find documents containing the text London that have an author field value of Reviewer.

You can achieve this result by submitting the following simple search expression:

```bash
search=London+author='Reviewer'
queryType=Simple
```
Alternatively, you can use an OData filter in a $filter parameter with a full Lucene search expression like this:

```bash
search=London
$filter=author eq 'Reviewer'
queryType=Full
```
## Filtering with facets
Facets are a useful way to present users with filtering criteria based on field values in a result set. They work best when a field has a small number of discrete values that can be displayed as links or options in the user interface.

To use facets, you must specify facetable fields for which you want to retrieve the possible values in an initial query. For example, you could use the following parameters to return all of the possible values for the author field:

```bash
search=*
facet=author
```
The results from this query include a collection of discrete facet values that you can display in the user interface for the user to select. Then in a subsequent query, you can use the selected facet value to filter the results:

```bash
search=*
$filter=author eq 'selected-facet-value-here'
```


## Persist extracted information in a knowledge store

While the index might be considered the primary output from an indexing process, the enriched data it contains might also be useful in other ways. For example:

- Since the index is essentially a collection of JSON objects, each representing an indexed record, it might be useful to export the objects as JSON files for integration into a data orchestration process for extract, transform, and load (ETL) operations.
- You may want to normalize the index records into a relational schema of tables for analysis and reporting.
- Having extracted embedded images from documents during the indexing process, you might want to save those images as files.

Azure AI Search supports these scenarios by enabling you to define a knowledge store in the skillset that encapsulates your enrichment pipeline. The knowledge store consists of projections of the enriched data, which can be JSON objects, tables, or image files. When an indexer runs the pipeline to create or update an index, the projections are generated and persisted in the knowledge store.