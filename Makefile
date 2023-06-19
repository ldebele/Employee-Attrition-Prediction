# install all dependencies
install:
	@python3 setup.py
	
# run main file
run:
	@streamlit run './scripts/main.py'