#!rebol -cs
REBOL []
print "Content-type: text/html^/"

html: make string! 2000
emit: func [data] [repend html data]

read-cgi: func [
    ;Read CGI data. Return data as string or NONE.
    /local data buffer
][
    switch system/options/cgi/request-method [
        "POST" [
            data: make string! 1020
            buffer: make string! 16380
            while [positive? read-io system/ports/input buffer 16380][
                append data buffer
                clear buffer
            ]
        ]
        "GET" [data: system/options/cgi/query-string]
    ]
    data
]

emit [
    <HTML><BODY BGCOLOR="#FFC080">
    <b> "CGI Form Data:" </b><p>
    "Submitted: " now <BR>
    "REBOL Version: " system/version <P>
    <TABLE BORDER="1" CELLSPACING="0" CELLPADDING="5">
]

foreach [var value] decode-cgi read-cgi [
    emit [<TR><TD> mold var </TD><TD> mold value </TD></TR>]
]

emit [</TABLE></BODY></HTML>]
print html