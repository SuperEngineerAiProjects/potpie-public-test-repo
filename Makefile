install:
	pip install -r requirements.txt

run:
	streamlit run simple_streamlit_app.py

dev:
	pip install -r requirements-dev.txt

test:
	pytest tests/

clean:
	rm -rf __pycache__ .pytest_cache