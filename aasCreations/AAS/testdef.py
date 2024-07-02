from basyx.aas import model
from basyx.aas.adapter import aasx
import create_aas_def 

asset,aas,aas_identifier =create_aas_def.create_aas('test')

submodel_nameplate = create_aas_def.create_submodel1()
aas.submodel.add(model.AASReference.from_referable(submodel_nameplate))
object_store = model.DictObjectStore([aas, asset, submodel_nameplate])
file_store = aasx.DictSupplementaryFileContainer()

with aasx.AASXWriter("test.aasx") as w:

        w.write_aas(aas_id=aas_identifier, object_store=object_store, file_store=file_store, submodel_split_parts=False)

