# Copyright 2025 Amazon Inc

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import time
from dataclasses import dataclass
from datetime import datetime as dt


@dataclass(frozen=True)
class ModelInput:
    image: str
    prompt: str
    active_url: str
    legacy_workflow_run_id: str = ""


@dataclass(frozen=True)
class ModelOutput:
    awl_raw_program: str


@dataclass(frozen=True)
class Step:
    model_input: ModelInput
    model_output: ModelOutput
    observed_time: dt
    rawMessage: dict[str, dict]

    @classmethod
    def from_message(cls, message: dict[str, dict]) -> "Step":
        # Extract input data
        input_data = message.get("input", {})
        model_input = ModelInput(
            image=input_data.get("screenshot", ""),
            prompt=input_data.get("prompt", ""),
            active_url=input_data.get("metadata", {}).get("activeURL", ""),
            legacy_workflow_run_id=input_data.get("agentRunCreate", {}).get("workflowRunId", ""),
        )

        # Extract output data
        output_data = message.get("output", {})
        model_output = ModelOutput(awl_raw_program=output_data.get("rawProgramBody", ""))

        # Extract timing data
        observed_time = dt.fromtimestamp(time.time())

        return cls(
            model_input=model_input,
            model_output=model_output,
            observed_time=observed_time,
            rawMessage=message,
        )

    # Input validation
    def __post_init__(self):
        """Validate instance after creation."""
        if not self.model_input.image:
            raise ValueError("Screenshot is required")
        if not self.model_output.awl_raw_program:
            raise ValueError("Program body is required")
