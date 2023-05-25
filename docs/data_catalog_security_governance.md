# Data Cataloging, Security, and Governance
- Data storage must comply with local laws for how the data should be handled,
- Data needs to be cataloged so that it is discoverable and useful to the organization.

## Definition
- **Data security** dictates how an organization should protect data to ensure that data is stored securely (such as in an encrypted state) and that access by unauthorized entities is prevented.
- **Data governance** is related to ensuring that only people that need access to specific datasets to perform their job is granted the access.
  - Governance also applies to ensuring that an organization only uses and processes data on individuals in approved ways and that organizations provide data disclosures as required by law.

## Data Privacy and Protection Regulations 
- The **General Data Protection Regulation (GDPR)** in the European Union: an organization is subject to the regulations if they hold data on any resident of the European Union, even if the organization does not have a legal presence in the EU.
    - an organization must appoint a Data Protection Officer (DPO). The DPO is responsible for training staff involved in data processing and conducting regular audits, among other responsibilities.
- The **California Consumer Privacy Act (CCPA)** and the recently passed California Privacy Rights Act (CPRA) in California, USA
- The **Personal Data Protection Bill (PDP Bill)** in India
- The **Protection of Personal Information Act (POPIA)** in South Africa
- Additional requirements to specific industries or functions:
    - The **Health Insurance Portability and Accountability Act (HIPAA)**, which applies to organizations that store an individual's healthcare and medical data
    - The **Payment Card Industry Data Security Standard (PCI DSS)**, which applies to organizations that store and process credit card data
- If you must participate in a compliance audit for an analytic workload running in AWS, review the  [AWS Artifact](https://aws.amazon.com/artifact/) service, a self-service portal for on-demand access to AWS's compliance reports.

## Core Data Protection Concepts 
- Summary:
    - Making sure PII data is replaced with a **token** as the first processing step after ingestion (and ensuring that the tokenization system is secure).
    - **Encrypting** all data at rest with a well-known and reliable encryption algorithm and ensuring that all connections use secure encrypted tunnels (such as by using the TLS protocol for all communications between systems).
    - Implementing **federated identities** where user authorization for analytic systems is performed via a central corporate identity provider, such as Active Directory. This ensures that, for example, when a user leaves the company and their Active Directory account is terminated, their access to analytic systems in AWS is terminated as a result.
    - Implementing **least privilege access**, where users are authorized for the minimum level of permissions that they need to perform their job.
### Personally Identifiable Information (PII)
- **Personally identifiable information (PII)** is a term commonly used in North America to reference any information that can be used to identify an individual.
    - PII also covers data that provides information about a specific aspect of an individual (such as a medical condition, location, or political affiliation).
### Personal Data
- **Personal data** is a term that is defined in GDPR and is considered to be similar to, but broader than, the definition of PII.
### Encryption
- **Encryption** is a mathematical technique of encoding data using a key in such a way that the data becomes unrecognizable and unusable. An authorized user who has the key used to encrypt the data can use the key to decrypt the data and return it to its original plaintext form.
    - Encrypted data may be able to be decrypted by a hacker without the key through the use of advanced computational resources, skills, and time. However, a well-designed and secure encryption algorithm increases the difficulty of decrypting the data without the key, increasing the security of the encrypted data.
    - There are two important types of encryption and both should be used for all data and systems:
        - **Encryption in transit**: This is the process of encrypting data as it moves between systems. For example, a system that migrates data from a database to a data lake should ensure that the data is encrypted before being transmitted, that the source and target endpoints are authenticated, and the data can then be decrypted at the target for processing. This helps ensure that if someone can intercept the data stream during transmission, that the data is encrypted and therefore unable to be read and used by the person who intercepted the data.
            - A common way to achieve this is to use the **Transport Layer Security (TLS)** protocol for all communications between systems.
        - **Encryption at rest**: This is the encryption of data that is written to a storage medium, such as a disk. After each phase of data processing, all the data that is persisted to disk should be encrypted.
### Anonymized Data
- **Anonymized data** is data that has been altered in such a way that personal data is irreversibly de-identified, rendering it impossible for any PII data to be identified.
    - For example, this could involve replacing PII data with randomly generated data, in such a way that the randomization cannot be reversed to recreate the original data.
    - Another way anonymization can be applied is to remove most of the PII data so that only a few attributes that may be considered PII remains, but with enough PII data removed to make it difficult to identify an individual.
### Pseudonymized data
- **Pseudonymized data** is data that has been altered in such a way that personal data is de-identified. While this is similar to the concept of anonymized data, the big difference is that with pseudonymized data, the original PII data can still be accessed.
    - For example, you can replace a full name with a randomly generated token, a different name (so that it looks real but is not), a hash representing the name, and more. However, whichever technique is used, it must be possible to still access the original data.
    - One of the most popular ways to do this is to have a tokenization system generate a unique, random token that replaces the PII data.
    - For example, when a raw dataset is ingested into the data lake, the first step may be to pass the data through the tokenization system. This system will replace all PII data in the dataset with an anonymous token, and will record each **real_data | token substitution** in a secure database. Once the data has been transformed, if a consumer requires access and is authorized to access the PII data, they can pass the dataset to the tokenization system to be detokenized (that is, have the tokens replaced with the original, real values).
    - If there is a data breach that can steal a dataset with tokenized data, there is no way to perform reverse engineering on the token to find the original value.
    - However, the tokenization system itself contains all the PII data, along with the associated tokens. If an entity can access the tokenized data and is also able to comprise the tokenization system, they will have access to all PII data. Therefore, it is important that the tokenization system is completely separate from the analytic systems containing the tokenized data, and that the tokenization system is protected properly.

### Hashing
- **Hashing** is generally considered the least secure method of de-identifying PII data, especially when it comes to data types with a limited set of values, such as social security numbers and names.
    - An original value, such as the name "John Smith," will always return the same hash value for a specific algorithm.
    - If you used the SHA-256 hashing algorithm to de-identify your PII data, it would be very easy for a malicious actor to determine that the preceding value referenced "John Smith" (just try Googling the preceding hash and see how quickly the name John Smith is revealed). While there are approaches to improving the security of a hash (such as salting the hash by adding a fixed string to the start of the value), it is still generally not recommended to use hashing for any data that has a well-known, limited set of values, or values that could be guessed.

### Authentication
- **Authentication** is the process of validating that a claimed identity is that identity.
    - Authentication does not specify what you can access but does attempt to validate that you are who you say you are.
    - Of course, authentication systems are not foolproof. Your password may have been compromised
    - If you have **multi-factor authentication (MFA)** enabled, you receive a code on your phone or a physical MFA device that you need to enter when logging in, and that helps to further secure and validate your identity.
    - **Federated identity** is a concept related to authentication and means that responsibility for authenticating a user is done by another system.
        - For example, when logging in to the AWS Management Console, your administrator could set up a federated identity so that you use your Active Directory credentials to log in via your organization's access portal, and the organization's Active Directory server authenticates you. Once authenticated, the Active Directory server confirms to the AWS Management Console that you have been successfully authenticated as a specific user. This means you do not need a separate username and password to log in to the AWS system, but that you can use your existing Active Directory credentials to be authenticated to an identity in AWS.
### Authorization
- **Authorization** is the process of authorizing access to a resource based on a validated identity.
    - For a data analytics system, once you validate your identity with authentication, you need to be authorized to access specific datasets. A data lake administrator can, for example, authorize you to access data that is in the Conformed Zone of the data lake, but not grant you access to data in the Raw Zone.


