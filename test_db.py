from database import engine

try:
    with engine.connect():
        print("✅ Conexión OK a PostgreSQL")
except Exception as e:
    print("❌ Error:", e)
