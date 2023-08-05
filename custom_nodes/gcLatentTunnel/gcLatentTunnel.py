import torch
import gc

class gcLatentTunnel:
    def __init__(self):
        pass
    
    @classmethod
    
    def INPUT_TYPES(s):
      return {
        "required": {
			  "samples": ("LATENT",),
		  }
	  }
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "gcTunnel"
    CATEGORY = "latent"

    def gcTunnel(self, samples):
        s = samples.copy()
        gc.collect()
        torch.cuda.empty_cache()
        torch.cuda.ipc_collect()
        return (s,)
      
NODE_CLASS_MAPPINGS = {
	"gcLatentTunnel": gcLatentTunnel,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "gcLatentTunnel": "LatentGarbageCollector"
}
