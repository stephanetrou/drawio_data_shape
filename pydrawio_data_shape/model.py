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
    MxGraphModel("source S3", COLOR.SOURCE, "Source S3", AWSStyle(20, 20, "mxgraph.aws4.s3", COLOR.AWS_STORAGE)),
    MxGraphModel("source rds", COLOR.SOURCE, "Source RDS", AWSStyle(20, 20, "mxgraph.aws4.rds", COLOR.AWS_DATABASE)),
    MxGraphModel(
        "source redshift",
        COLOR.SOURCE,
        "Source Redshift",
        AWSStyle(20, 20, "mxgraph.aws4.redshift", COLOR.AWS_DATABASE),
    ),
    MxGraphModel(
        "source dynamodb",
        COLOR.SOURCE,
        "Source DynamoDB",
        AWSStyle(20, 20, "mxgraph.aws4.dynamodb", COLOR.AWS_DATABASE),
    ),
    MxGraphModel(
        "source glue", COLOR.SOURCE, "Source Glue", AWSStyle(20, 20, "mxgraph.aws4.glue", COLOR.AWS_ANALYTICS)
    ),
    MxGraphModel(
        "source athena", COLOR.SOURCE, "Source Athena", AWSStyle(20, 20, "mxgraph.aws4.athena", COLOR.AWS_ANALYTICS)
    ),
    MxGraphModel("Source api", COLOR.SOURCE, "Source API", ImageStyle(15, 19, "img/lib/mscae/API_Management.svg")),
    # Models
    MxGraphModel("model S3", COLOR.MODEL, "Model S3", AWSStyle(20, 20, "mxgraph.aws4.s3", COLOR.AWS_STORAGE)),
    MxGraphModel("model rds", COLOR.MODEL, "Model RDS", AWSStyle(20, 20, "mxgraph.aws4.rds", COLOR.AWS_DATABASE)),
    MxGraphModel(
        "model redshift", COLOR.MODEL, "Model Redshift", AWSStyle(20, 20, "mxgraph.aws4.redshift", COLOR.AWS_DATABASE)
    ),
    MxGraphModel(
        "model dynamodb", COLOR.MODEL, "Model DynamoDB", AWSStyle(20, 20, "mxgraph.aws4.dynamodb", COLOR.AWS_DATABASE)
    ),
    # Consumers
    MxGraphModel(
        "consumer powerbi",
        COLOR.CONSUMER,
        "Consumer PowerBI",
        ImageStyle(20, 15, "img/lib/azure2/analytics/Power_BI_Embedded.svg"),
    ),
    MxGraphModel(
        "consumer api",
        COLOR.CONSUMER,
        "Consumer API",
        ImageStyle(15, 19, "img/lib/azure2/integration/API_Management_Services.svg"),
    ),
]
