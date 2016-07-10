CC = gcc
BIN = bin
SRCS = $(wildcard *.c)
BINS = $(addprefix $(BIN)/, $(SRCS:.c=))

all: $(BINS)

$(BIN)/%: %.c
	@mkdir -p $(BIN)
	$(CC) -o $@ $<
	
clean:
	$(RM) -r $(BIN)
