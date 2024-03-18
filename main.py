import os
import PyPDF3
from gtts import gTTS
from tkinter import filedialog, Tk
import sys


def extract_text_from_pdf(pdf_file):
	"""Extract Text from PDF"""
	text = ""
	with open(pdf_file, "rb") as f:
		reader = PyPDF3.PdfFileReader(f)
		num_pages = reader.numPages
		for page_no in range(num_pages):
			page = reader.getPage(page_no)
			text += page.extractText()
	return text


def convert_text_to_audio(text, audio_file, language="en"):
	"""Coverts Text to Audio File"""
	tts = gTTS(text=text, lang=language, slow=False)
	tts.save(audio_file)


def pick_output_directory():
	root = Tk()
	root.withdraw()  # Hide the main window
	# Open directory dialog to pick output directory
	output_directory = filedialog.askdirectory()
	return output_directory


def main(pdf_file, audio_file):
	"""Extract Text From PDF & Convert Text to Audio"""
	# Extract text from PDF
	text = extract_text_from_pdf(pdf_file)
	# Covert Text to Audio
	convert_text_to_audio(text, audio_file)
	print("Conversion Completed")
	sys.exit()


def open_pdf():
	root = Tk()
	root.withdraw()  # Hide the Tk window
	# Open file dialog to pick PDF file
	file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
	return file_path


if __name__ == "__main__":
	# Pick PDF file
	pdf_file = open_pdf()

	if pdf_file:
		# Extract file name without extension
		file_name = os.path.splitext(os.path.basename(pdf_file))[0]

		# Specify the output directory
		output_directory = pick_output_directory()

		if output_directory:
			# Output Audio File
			audio_file = os.path.join(output_directory, f"{file_name}.mp3")

			# Process PDF file
			main(pdf_file, audio_file)
		else:
			print("No output directory selected")
	else:
		print("No PDF file selected.")
