from pathlib import Path
from typing import Any, DefaultDict, List, Mapping, Optional

from datamodel_code_generator.imports import Import
from datamodel_code_generator.model.base import DataModel, DataModelField
from datamodel_code_generator.model.pydantic.types import get_data_type
from datamodel_code_generator.types import DataType, Types


class CustomRootType(DataModel):
    TEMPLATE_FILE_PATH = 'pydantic/BaseModel_root.jinja2'
    BASE_CLASS = 'pydantic.BaseModel'

    def __init__(
        self,
        name: str,
        fields: List[DataModelField],
        decorators: Optional[List[str]] = None,
        base_classes: Optional[List[str]] = None,
        custom_base_class: Optional[str] = None,
        custom_template_dir: Optional[Path] = None,
        extra_template_data: Optional[DefaultDict[str, Any]] = None,
        imports: Optional[List[Import]] = None,
        auto_import: bool = True,
        reference_classes: Optional[List[str]] = None,
    ):
        super().__init__(
            name,
            fields=fields,
            decorators=decorators,
            base_classes=base_classes,
            custom_base_class=custom_base_class,
            custom_template_dir=custom_template_dir,
            extra_template_data=extra_template_data,
            imports=imports,
            auto_import=auto_import,
            reference_classes=reference_classes,
        )

    @classmethod
    def get_data_type(cls, types: Types, **kwargs: Any) -> DataType:
        return get_data_type(types, **kwargs)
