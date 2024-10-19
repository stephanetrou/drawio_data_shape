from dataclasses import dataclass

from pydrawio_data_shape.color import COLOR


@dataclass(frozen=True)
class Style:
    height: int
    width: int


@dataclass(frozen=True)
class AWSStyle(Style):
    shape_icon: str
    shape_icon_color: COLOR
    shape_group_icon: str = "mxgraph.aws4.resourceIcon"


@dataclass(frozen=True)
class ImageStyle(Style):
    image: str


class AWSStyles:
    S3 = AWSStyle(20, 20, "mxgraph.aws4.s3", COLOR.AWS_STORAGE)
    RDS = AWSStyle(20, 20, "mxgraph.aws4.rds", COLOR.AWS_DATABASE)
    REDSHIFT = AWSStyle(20, 20, "mxgraph.aws4.redshift", COLOR.AWS_DATABASE)
    DYNAMODB = AWSStyle(20, 20, "mxgraph.aws4.dynamodb", COLOR.AWS_DATABASE)
    GLUE = AWSStyle(20, 20, "mxgraph.aws4.glue", COLOR.AWS_ANALYTICS)
    ATHENA = AWSStyle(20, 20, "mxgraph.aws4.athena", COLOR.AWS_ANALYTICS)


class OnPremStyles:
    ORACLE = AWSStyle(20, 20, "mxgraph.aws4.database", COLOR.ORACLE)
    ORACLE_MINI = AWSStyle(16, 20, "mxgraph.office.databases.database_mini_2", COLOR.ORACLE)


class AzureStyles:
    API = ImageStyle(15, 19, "img/lib/azure2/integration/API_Management_Services.svg")
    POWER_BI = ImageStyle(20, 15, "img/lib/azure2/analytics/Power_BI_Embedded.svg")
    CUBE_BLUE = AWSStyle(20, 18, "mxgraph.office.databases.database_cube", COLOR.CUBE_BLUE)
    BLOB = ImageStyle(17, 20, "img/lib/mscae/BlobBlock.svg")
    SQL_DATA_WAREHOUSE = ImageStyle(20, 20, "img/lib/azure2/databases/SQL_Data_Warehouses.svg")
    SQL_SERVER = ImageStyle(20, 20, "img/lib/azure2/databases/SQL_Server.svg")


@dataclass(frozen=True)
class MxGraphModel:
    title: str
    shape_color: COLOR
    placeholder: str
    style: Style
    width: int = 210
    height: int = 70
    aspect: str = "fixed"


MX_GRAPH_MODELS = [
    # Sources
    MxGraphModel("source S3", COLOR.SOURCE, "Source S3", AWSStyles.S3),
    MxGraphModel("source rds", COLOR.SOURCE, "Source RDS", AWSStyles.RDS),
    MxGraphModel("source redshift", COLOR.SOURCE, "Source Redshift", AWSStyles.REDSHIFT),
    MxGraphModel("source dynamodb", COLOR.SOURCE, "Source DynamoDB", AWSStyles.DYNAMODB),
    MxGraphModel("source glue", COLOR.SOURCE, "Source Glue", AWSStyles.GLUE),
    MxGraphModel("source athena", COLOR.SOURCE, "Source Athena", AWSStyles.ATHENA),
    MxGraphModel("Source api", COLOR.SOURCE, "Source API", AzureStyles.API),
    MxGraphModel("source blob storage", COLOR.SOURCE, "Source Blob Storage", AzureStyles.BLOB),
    MxGraphModel(
        "source sql data warehouse", COLOR.SOURCE, "Source SQL Data Warehouse", AzureStyles.SQL_DATA_WAREHOUSE
    ),
    MxGraphModel("source sql server", COLOR.SOURCE, "Source SQL Server", AzureStyles.SQL_SERVER),
    MxGraphModel("source oracle", COLOR.SOURCE, "Source Oracle", OnPremStyles.ORACLE),
    MxGraphModel("source oracle mini", COLOR.SOURCE, "Source Oracle", OnPremStyles.ORACLE_MINI),
    # Models
    MxGraphModel("model S3", COLOR.MODEL, "Model S3", AWSStyles.S3),
    MxGraphModel("model rds", COLOR.MODEL, "Model RDS", AWSStyles.RDS),
    MxGraphModel("model redshift", COLOR.MODEL, "Model Redshift", AWSStyles.REDSHIFT),
    MxGraphModel("model dynamodb", COLOR.MODEL, "Model DynamoDB", AWSStyles.DYNAMODB),
    # Consumers
    MxGraphModel("consumer powerbi", COLOR.CONSUMER, "Consumer PowerBI", AzureStyles.POWER_BI),
    MxGraphModel("consumer cube blue", COLOR.CONSUMER, "Cube", AzureStyles.CUBE_BLUE),
    MxGraphModel("consumer api", COLOR.CONSUMER, "Consumer API", AzureStyles.API),
    MxGraphModel("consumer sql server", COLOR.CONSUMER, "Consumer SQL Server", AzureStyles.SQL_SERVER),
]
