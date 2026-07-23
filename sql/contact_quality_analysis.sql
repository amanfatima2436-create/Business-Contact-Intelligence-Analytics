-- ============================================
-- Business Contact Intelligence Analytics
-- Contact Quality Analysis
-- ============================================


-- 1. Contact Completeness Distribution
SELECT
    contact_completeness,
    COUNT(*) AS total_contacts
FROM business_contacts
GROUP BY contact_completeness
ORDER BY contact_completeness;


-- 2. Complete Contact Records
SELECT
    COUNT(*) AS complete_contacts
FROM business_contacts
WHERE contact_completeness = 2;


-- 3. Incomplete Contact Records
SELECT
    law_firms_name,
    first_name,
    last_name,
    title,
    phone_number,
    email,
    contact_completeness
FROM business_contacts
WHERE contact_completeness < 2;


-- 4. Contacts Missing Phone Number
SELECT
    law_firms_name,
    first_name,
    last_name,
    title,
    email
FROM business_contacts
WHERE phone_number IS NULL;


-- 5. Contacts Missing Email
SELECT
    law_firms_name,
    first_name,
    last_name,
    title,
    phone_number
FROM business_contacts
WHERE email IS NULL;


-- 6. Data Enrichment Priority Distribution
SELECT
    enrichment_priority,
    COUNT(*) AS total_contacts
FROM business_contacts
GROUP BY enrichment_priority
ORDER BY
    CASE enrichment_priority
        WHEN 'High Priority' THEN 1
        WHEN 'Medium Priority' THEN 2
        WHEN 'Low Priority' THEN 3
    END;


-- 7. Contacts Requiring Data Enrichment
SELECT
    law_firms_name,
    first_name,
    last_name,
    title,
    phone_number,
    email,
    enrichment_priority
FROM business_contacts
WHERE enrichment_priority != 'Low Priority'
ORDER BY
    CASE enrichment_priority
        WHEN 'High Priority' THEN 1
        WHEN 'Medium Priority' THEN 2
        WHEN 'Low Priority' THEN 3
    END;