# Athenaeum
```
Athenaeum
├─ .kilo
│  └─ worktrees
│     └─ boulder-spacecraft
│        ├─ LICENSE
│        ├─ README.md
│        ├─ backend
│        │  ├─ Dockerfile
│        │  ├─ alembic
│        │  │  ├─ README
│        │  │  ├─ env.py
│        │  │  ├─ script.py.mako
│        │  │  └─ versions
│        │  │     ├─ 07b4ee6b4560_create_refresh_tokens_table.py
│        │  │     ├─ 4d5ff8e510f3_create_knowledge_items_table.py
│        │  │     ├─ 594dca574bb8_add_document_chunks.py
│        │  │     ├─ 6ab18ed8c60a_add_user_role.py
│        │  │     ├─ 8d6a3a8917f4_create_users_table.py
│        │  │     ├─ acfac48b01ee_create_knowledge_items_table.py
│        │  │     └─ e0761e4ada23_add_updated_at_to_knowledge_items.py
│        │  ├─ alembic.ini
│        │  ├─ app
│        │  │  ├─ __init__.py
│        │  │  ├─ api
│        │  │  │  ├─ __init__.py
│        │  │  │  └─ v1
│        │  │  │     ├─ __init__.py
│        │  │  │     └─ routes
│        │  │  │        ├─ __init__.py
│        │  │  │        ├─ auth.py
│        │  │  │        ├─ knowledge.py
│        │  │  │        ├─ redis.py
│        │  │  │        └─ users.py
│        │  │  ├─ core
│        │  │  │  ├─ __init__.py
│        │  │  │  ├─ config.py
│        │  │  │  └─ security.py
│        │  │  ├─ db
│        │  │  │  ├─ __init__.py
│        │  │  │  ├─ database.py
│        │  │  │  ├─ models
│        │  │  │  │  ├─ __init__.py
│        │  │  │  │  ├─ document_chunk.py
│        │  │  │  │  ├─ knowledge_item.py
│        │  │  │  │  ├─ refresh_token.py
│        │  │  │  │  └─ user.py
│        │  │  │  └─ session.py
│        │  │  ├─ main.py
│        │  │  ├─ redis_client.py
│        │  │  ├─ schemas
│        │  │  │  ├─ auth.py
│        │  │  │  ├─ knowledge_item.py
│        │  │  │  └─ user.py
│        │  │  └─ services
│        │  │     ├─ auth_services.py
│        │  │     ├─ chunk_services.py
│        │  │     ├─ document_services.py
│        │  │     ├─ knowledge_services.py
│        │  │     ├─ redis_services.py
│        │  │     └─ user_services.py
│        │  └─ requirements.txt
│        ├─ docker-compose.yml
│        └─ package.json
├─ LICENSE
├─ README.md
├─ backend
│  ├─ Dockerfile
│  ├─ alembic
│  │  ├─ README
│  │  ├─ env.py
│  │  ├─ script.py.mako
│  │  └─ versions
│  │     ├─ 07b4ee6b4560_create_refresh_tokens_table.py
│  │     ├─ 4d5ff8e510f3_create_knowledge_items_table.py
│  │     ├─ 594dca574bb8_add_document_chunks.py
│  │     ├─ 6ab18ed8c60a_add_user_role.py
│  │     ├─ 8d6a3a8917f4_create_users_table.py
│  │     ├─ acfac48b01ee_create_knowledge_items_table.py
│  │     ├─ e0761e4ada23_add_updated_at_to_knowledge_items.py
│  │     └─ f669d7697425_add_document_chunk_embeddings.py
│  ├─ alembic.ini
│  ├─ app
│  │  ├─ __init__.py
│  │  ├─ api
│  │  │  ├─ __init__.py
│  │  │  └─ v1
│  │  │     ├─ __init__.py
│  │  │     └─ routes
│  │  │        ├─ __init__.py
│  │  │        ├─ auth.py
│  │  │        ├─ knowledge.py
│  │  │        ├─ redis.py
│  │  │        ├─ search.py
│  │  │        └─ users.py
│  │  ├─ core
│  │  │  ├─ __init__.py
│  │  │  ├─ config.py
│  │  │  └─ security.py
│  │  ├─ db
│  │  │  ├─ __init__.py
│  │  │  ├─ database.py
│  │  │  ├─ models
│  │  │  │  ├─ __init__.py
│  │  │  │  ├─ document_chunk.py
│  │  │  │  ├─ knowledge_item.py
│  │  │  │  ├─ refresh_token.py
│  │  │  │  └─ user.py
│  │  │  └─ session.py
│  │  ├─ main.py
│  │  ├─ redis_client.py
│  │  ├─ schemas
│  │  │  ├─ auth.py
│  │  │  ├─ knowledge_item.py
│  │  │  ├─ search.py
│  │  │  └─ user.py
│  │  ├─ services
│  │  │  ├─ auth_services.py
│  │  │  ├─ chunk_services.py
│  │  │  ├─ document_services.py
│  │  │  ├─ embedding_services.py
│  │  │  ├─ knowledge_services.py
│  │  │  ├─ redis_services.py
│  │  │  ├─ search_services.py
│  │  │  └─ user_services.py
│  │  └─ utils
│  ├─ requirements.txt
│  └─ tests
├─ docker
│  ├─ nginx
│  ├─ postgres
│  └─ redis
├─ docker-compose.yml
├─ frontend
├─ ml-services
└─ package.json

```