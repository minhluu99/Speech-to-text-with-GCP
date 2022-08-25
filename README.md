# Transcribe-Audio-to-Text-with-Split-Function

As recently reported, a paperless meeting software was created by the DATA & AI department of the Institute for Research and Innovation in Computer Science (IRICS) in cooperation with STECH Technology & Engineering JSC as part of a strategic cooperation project between the Army Software Park and the IRICS Institute and STECH JSC. The Vietnam People’s Army uses this program for both offline and online conferences, which uses artificial intelligence technology and comprehensive security. This technology is also known collectively as “Speech to text”.

So what exactly is “Speech to text” and what are its operating principles? IRICS will provide you with the following technical knowledge:

WHAT IS SPEECH TO TEXT?

Speech to text is a speech recognition software that enables the recognition and conversion of spoken language into text through computational linguistics. Speech to text is also known as speech recognition or computer speech recognition. Certain applications, tools, and devices can instantly transcribe audio streams into text for processing and display.

Simple isn't it? So what tasks are ‘Speech to text’ used for?

This technology is widely used in English-speaking countries but is not yet common in Vietnam. Voice-to-text technology has rapidly expanded from daily phone use (Apple’s Siri) to sectors in marketing, banking, and healthcare. Speech recognition software shows how speech-to-text technology can expand beyond routine jobs and improve the efficiency of more complex ones.

What is my demo ?
I transcribe Audio with Split Function associated with Google Cloud Speech-To API. To trim long audio, if its durations are longer than 1 minutes, then the processing will faster. For audio longer than 1 minutes, you need to send it to Google Cloud, it may take longer time for long audio. 
After Audio split speakers with Agglomerative Clustering Algorithm, audio is processed with silences time no longer than 500 ms & accurately convert speech into text with an API via Google Cloud
