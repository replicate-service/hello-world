import io
import cog
import tempfile
from PIL import Image
from pathlib import Path


class Predictor(cog.Predictor):
    def setup(self):
        self.prefix = "hello"

    @cog.input("prompts", type=str, help="text prompt")
    @cog.input("settings", type=str, help="yaml settings", default="default_settings")
    def predict(self, prompts, settings):
        print(prompts)
        print(settings)
        img = Image.new('RGB', (width, height))
        out_path = Path(tempfile.mkdtemp()) / "out.png"
        im.save(str(out_path))
        return out_path
