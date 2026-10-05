# Deployment

Milestone 1 preserves the static HTTP reader, with public practice answers and browser state. It is not a secure exam system.

Milestone 2 introduces Docker Compose/PostgreSQL migrations. Production guidance requires a separate Compose example, secrets, reverse proxy, HTTPS/domain configuration and tested backup/restore procedures before deployment can be recommended.

No fixed cloud provider/domain is required. Operators provision credentials outside Git, disable development conveniences, protect learner records and store provider keys/exam specs privately. Actual commands and deployment limitations are recorded in [VALIDATION_REPORT.md](VALIDATION_REPORT.md).
