import io
import time
import tempfile
from pydantic import BaseModel
from cog import Predictor, Input, Path, File

class Output(BaseModel):
    file: File


class Predictor(Predictor):
    def setup(self):
        print("Preparing model")
        self.foo = "foo"

    def predict(self,
                prompts: str = Input(title="text prompt"),
                settings: str = Input(title="yaml settings")
    ) -> str:
        print("Predicting " + prompts)
        return Output(file=io.StringIO("output_file"))
