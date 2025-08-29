FROM alpine:3.20

RUN apk add --no-cache bash curl

COPY wikiTodo.sh /usr/local/bin/wikiTodo.sh
RUN chmod +x /usr/local/bin/wikiTodo.sh

CMD ["/usr/local/bin/wikiTodo.sh"]
