import ffmpeg


class FFMPEGConverter:

    @staticmethod
    def convert_webm(input_file, output_file):
        try:
            stream = ffmpeg.input(input_file)
            final_stream = ffmpeg.output(stream, output_file)
            ffmpeg.run(final_stream)
        except:
            print('Error')


convertor = FFMPEGConverter()

convertor.convert_webm(r'C:\User\Videos\Somefile.webm', r'C:\User\Videos\Somefile.mp4')
