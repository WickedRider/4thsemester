
FLAGS  = -Wall -g
CC     = gcc
PROG   = example02
OBJS   = example02.o queue.o

all:	${PROG}

clean:
	rm ${OBJS} ${PROG} *~
  
${PROG}:	${OBJS}
	${CC} ${FLAGS} ${OBJS} -o $@

.c.o:
	${CC} ${FLAGS} $< -c

##########################

queue.o:  queue.h queue.c

example02.o: queue.h example02.c

example02: queue.o example02.o

