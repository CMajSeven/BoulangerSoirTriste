SRC_DIR = ../old
SRC_DIR2 = ../base
SRCS := $(wildcard $(SRC_DIR)/*.png)
DSTS := $(subst $(SRC_DIR),.,$(SRCS))
SEMICLEAN_CMD := (powershell -ExecutionPolicy Bypass -File ./semiclean.ps1 -InDir $(SRC_DIR)) || touch status


all: $(DSTS) status
	$(SEMICLEAN_CMD)

# force image to fit in screen bounds and rotate it so that -spl can use them
./%.png:: $(SRC_DIR)/%.png $(SRC_DIR2)/%.png
	python align.py $< $(SRC_DIR2)/$(notdir $<) $(notdir $<)

clean:
	rm -f *.png || true
	
status:
	touch status

# clean out images derived from spl images that no longer exist and update status file if files were deleted
semiclean: status
	$(SEMICLEAN_CMD)