FOLDERS := lab2 lab3
.PHONY: $(FOLDERS) update-pipfile

$(FOLDERS):
	@cd $(@) && pipenv lock --clear

update-pipfile: $(FOLDERS)

clean:
	@find . -name ".pytest_cache" -type d -exec rm -rf "{}" +
