.PHONY: migration
migration:
	alembic revision \
	  --autogenerate \
	  --message $(message)

.PHONY: migrate
migrate:
	alembic upgrade head

.PHONY: createsuperadmin
createsuperadmin:
	python3 createsuperadmin.py