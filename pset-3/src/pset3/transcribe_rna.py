"""Rosalind RNA: Transcribing DNA into RNA."""

def transcribeRNA(text: str) -> str:
    RNA_text = ""

    x = 0

    while(x < len(text)):
        if(text[x:x+1] == "T"):
            RNA_text = RNA_text+"U"
        else:
            RNA_text = RNA_text+(text[x:x+1])

        x = x+1

    return RNA_text