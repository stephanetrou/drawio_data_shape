from dataclasses import dataclass

from drawio_data_shape.color import COLOR


@dataclass(frozen=True)
class Datasource:
    height: int
    width: int


@dataclass(frozen=True)
class IconDatasource(Datasource):
    shape_icon: str
    shape_icon_color: COLOR
    shape_group_icon: str = "mxgraph.aws4.resourceIcon"


@dataclass(frozen=True)
class ImageDatasource(Datasource):
    image: str


class AWSThemes:
    S3 = IconDatasource(20, 20, "mxgraph.aws4.s3", COLOR.AWS_STORAGE)
    RDS = IconDatasource(20, 20, "mxgraph.aws4.rds", COLOR.AWS_DATABASE)
    REDSHIFT = IconDatasource(20, 20, "mxgraph.aws4.redshift", COLOR.AWS_DATABASE)
    DYNAMODB = IconDatasource(20, 20, "mxgraph.aws4.dynamodb", COLOR.AWS_DATABASE)
    GLUE = IconDatasource(20, 20, "mxgraph.aws4.glue", COLOR.AWS_ANALYTICS)
    ATHENA = IconDatasource(20, 20, "mxgraph.aws4.athena", COLOR.AWS_ANALYTICS)


class OnPremTheme:
    ORACLE = IconDatasource(20, 20, "mxgraph.aws4.database", COLOR.ORACLE)


class AzureThemes:
    API = ImageDatasource(12, 19, "img/lib/azure2/integration/API_Management_Services.svg")
    POWER_BI = ImageDatasource(20, 15, "img/lib/azure2/analytics/Power_BI_Embedded.svg")
    CUBE_BLUE = ImageDatasource(20, 18, "img/lib/active_directory/database_cube.svg")
    BLOB = ImageDatasource(17, 20, "img/lib/mscae/BlobBlock.svg")
    SQL_DATA_WAREHOUSE = ImageDatasource(20, 20, "img/lib/azure2/databases/SQL_Data_Warehouses.svg")
    SQL_SERVER = ImageDatasource(20, 20, "img/lib/azure2/databases/SQL_Server.svg")


@dataclass(frozen=True)
class TemplateDetails:
    title: str
    shape_color: COLOR
    placeholder: str
    style: Datasource
    width: int = 210
    height: int = 70
    aspect: str = "fixed"


MX_GRAPH_MODELS = [
    # Sources
    TemplateDetails("source S3", COLOR.SOURCE, "Source S3", AWSThemes.S3),
    TemplateDetails("source rds", COLOR.SOURCE, "Source RDS", AWSThemes.RDS),
    TemplateDetails("source redshift", COLOR.SOURCE, "Source Redshift", AWSThemes.REDSHIFT),
    TemplateDetails("source dynamodb", COLOR.SOURCE, "Source DynamoDB", AWSThemes.DYNAMODB),
    TemplateDetails("source glue", COLOR.SOURCE, "Source Glue", AWSThemes.GLUE),
    TemplateDetails("source athena", COLOR.SOURCE, "Source Athena", AWSThemes.ATHENA),
    TemplateDetails("Source api", COLOR.SOURCE, "Source API", AzureThemes.API),
    TemplateDetails("source blob storage", COLOR.SOURCE, "Source Blob Storage", AzureThemes.BLOB),
    TemplateDetails(
        "source sql data warehouse", COLOR.SOURCE, "Source SQL Data Warehouse", AzureThemes.SQL_DATA_WAREHOUSE
    ),
    TemplateDetails("source sql server", COLOR.SOURCE, "Source SQL Server", AzureThemes.SQL_SERVER),
    TemplateDetails("source oracle", COLOR.SOURCE, "Source Oracle", OnPremTheme.ORACLE),
    # Models
    TemplateDetails("model S3", COLOR.MODEL, "Model S3", AWSThemes.S3),
    TemplateDetails("model rds", COLOR.MODEL, "Model RDS", AWSThemes.RDS),
    TemplateDetails("model redshift", COLOR.MODEL, "Model Redshift", AWSThemes.REDSHIFT),
    TemplateDetails("model dynamodb", COLOR.MODEL, "Model DynamoDB", AWSThemes.DYNAMODB),
    # Consumers
    TemplateDetails("consumer powerbi", COLOR.CONSUMER, "Consumer PowerBI", AzureThemes.POWER_BI),
    TemplateDetails("consumer cube blue", COLOR.CONSUMER, "Cube", AzureThemes.CUBE_BLUE),
    TemplateDetails("consumer api", COLOR.CONSUMER, "Consumer API", AzureThemes.API),
    TemplateDetails("consumer sql server", COLOR.CONSUMER, "Consumer SQL Server", AzureThemes.SQL_SERVER),
]


@dataclass(frozen=True)
class MedallionTemplate:
    title: str
    shape_color: COLOR
    width: int = 16
    height: int = 16
    aspect: str = "fixed"


MEDALLIONS = [
    MedallionTemplate("Bronze", COLOR.BRONZE),
    # MedallionTemplate("Dark Bronze", COLOR.DARK_BRONZE),
    MedallionTemplate("Silver", COLOR.SILVER),
    MedallionTemplate("Gold", COLOR.GOLD),
    # MedallionTemplate("Platinum", COLOR.PLATINUM),
    MedallionTemplate("Diamond", COLOR.DIAMOND),
    # MedallionTemplate("Light Diamond", COLOR.LIGHT_DIAMOND),
]
