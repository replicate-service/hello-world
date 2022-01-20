import cog

class Predictor(cog.Predictor):
    def setup(self):
        self.prefix = "hello"

    @cog.input("prompts", type=str, help="text prompt")
    @cog.input("settings", type=str, help="yaml settings", default="default_settings")
    def predict(self, input):
        return io.StringIO("output_file")
