from marshmallow import Schema
from typing import Dict

from domain.model.publication import PublicationType
from .alteration_license import AlterationLicenseSchema
from .animal_handling import AnimalHandlingSchema
from .cancel_ordinance import CancelOrdinanceSchema
from .condition_review import ConditionReviewSchema
from .environmental_authorization import EnvironmentalAuthorizationSchema
from .erratum import ErratumSchema
from .exploration_approval import ExplorationApprovalSchema
from .extended_term import ExtendedTermSchema
from .forest_management import ForestManagementSchema
from .forest_replacement_credit import ForestReplacementCreditSchema
from .forest_volume_credit import ForestVolumeCreditSchema
from .forest_volume_recognition import ForestVolumeRecognitionSchema
from .forest_volume_transfer import ForestVolumeTransferSchema
from .grant_waiver import GrantWaiverSchema
from .installation_license import InstallationLicenseSchema
from .license_cancellation import LicenseCancellationSchema
from .license_renewal import LicenseRenewalSchema
from .license_revocation import LicenseRevocationSchema
from .location_license import LocationLicenseSchema
from .operation_license import OperationLicenseSchema
from .owner_name_change import OwnerNameChangeSchema
from .ownership_transfer import OwnershipTransferSchema
from .planting_anticipation import PlantingAnticipationSchema
from .preliminary_license import PreliminaryLicenseSchema
from .regularization_license import RegularizationLicenseSchema
from .right_use_water_resources import RightUseWaterResourcesSchema
from .special_procedure import SpecialProcedureSchema
from .unified_license import UnifiedLicenseSchema
from .vegetal_suppression import VegetalSuppressionSchema
from .owner_correction import OwnerCorrectionSchema
from .implantation_license import ImplantationLicenseSchema
from .infraction_warning import InfractionWarningSchema
from .interdiction_infraction import InterdictionInfractionSchema
from .demolition_penalty import DemolitionPenaltySchema
from .fine_infraction import FineInfractionSchema
from .seizure_infraction import SeizureInfractionSchema
from .active_debit import ActiveDebitSchema
from .grant_process import GrantProcessSchema
from .process_extinction import ProcessExtinctionSchema
from .anticipated_environ_license import AnticipatedEnvironmentalLicenseSchema # noqa
from .notification_notice import NotificationNotice
from .simplified_environmental_license import SimplifiedEnvironmentalLicenseSchema # noqa
from .deadline_extension import DeadlineExtensionSchema
from .rectification import RectificationSchema
from .order_revocation import OrderRevocationSchema
from .seizure import SeizureSchema
from .degraded_area_recovery_plan import DegradedAreaRecoveryPlanSchema
from .grant_environmental_license import GrantEnvironmentalLicenseSchema
from .administrative_decision import AdministrativeDecisionSchema
from .conformity_certificate import ConformityCertificateSchema
from .ibama_infraction_notice import IbamaInfractionNoticeSchema
from .icmbio_infraction_notice import ICMBioInfractionNoticeSchema
from .right_use_water_renovation import RightUseWaterResourcesRenovationSchema
from .right_use_water_resource_change import RightUseWaterResourceChangeSchema

publication_types: Dict[PublicationType, Schema] = {
    PublicationType.ACTIVE_DEBIT: ActiveDebitSchema(),
    PublicationType.ADMINISTRATIVE_DECISION: AdministrativeDecisionSchema(),
    PublicationType.ALTERATION_LICENSE: AlterationLicenseSchema(),
    PublicationType.ANIMAL_HANDLING: AnimalHandlingSchema(),
    PublicationType.ANTICIPATED_ENVIRONMENTAL_LICENSE: AnticipatedEnvironmentalLicenseSchema(), # noqa
    PublicationType.CANCEL_: CancelOrdinanceSchema(),
    PublicationType.CONDITION_REVIEW: ConditionReviewSchema(),
    PublicationType.ENVIRONMENTAL_AUTHORIZATION: EnvironmentalAuthorizationSchema(), # noqa
    PublicationType.ERRATUM: ErratumSchema(),
    PublicationType.EXPLORATION_APPROVAL: ExplorationApprovalSchema(),
    PublicationType.EXTENDED_TERM: ExtendedTermSchema(),
    PublicationType.FOREST_MANAGEMENT: ForestManagementSchema(),
    PublicationType.FOREST_REPLACEMENT_CREDIT: ForestReplacementCreditSchema(),
    PublicationType.FOREST_VOLUME_CREDIT: ForestVolumeCreditSchema(),
    PublicationType.FOREST_VOLUME_RECOGNITION: ForestVolumeRecognitionSchema(),
    PublicationType.FOREST_VOLUME_TRANSFER: ForestVolumeTransferSchema(),
    PublicationType.GRANT_WAIVER: GrantWaiverSchema(),
    PublicationType.IMPLANTATION_LICENSE: ImplantationLicenseSchema(),
    PublicationType.INFRACTION_WARNING: InfractionWarningSchema(),
    PublicationType.INSTALLATION_LICENSE: InstallationLicenseSchema(),
    PublicationType.INTERDICTION_INFRACTION: InterdictionInfractionSchema(),
    PublicationType.LICENSE_CANCELLATION: LicenseCancellationSchema(),
    PublicationType.LICENSE_RENEWAL: LicenseRenewalSchema(),
    PublicationType.LICENSE_REVOCATION: LicenseRevocationSchema(),
    PublicationType.LOCATION_LICENSE: LocationLicenseSchema(),
    PublicationType.OPERATION_LICENSE: OperationLicenseSchema(),
    PublicationType.OWNER_CORRECTION: OwnerCorrectionSchema(),
    PublicationType.OWNER_NAME_CHANGE: OwnerNameChangeSchema(),
    PublicationType.OWNERSHIP_TRANSFER: OwnershipTransferSchema(),
    PublicationType.PLANTING_ANTICIPATION: PlantingAnticipationSchema(),
    PublicationType.PRELIMINARY_LICENSE: PreliminaryLicenseSchema(),
    PublicationType.REGULARIZATION_LICENSE: RegularizationLicenseSchema(),
    PublicationType.RIGHT_USE_WATER_RESOURCES: RightUseWaterResourcesSchema(),
    PublicationType.SPECIAL_PROCEDURE: SpecialProcedureSchema(),
    PublicationType.UNIFIED_LICENSE: UnifiedLicenseSchema(),
    PublicationType.VEGETAL_SUPPRESSION: VegetalSuppressionSchema(),
    PublicationType.DEMOLITION_PENALTY: DemolitionPenaltySchema(),
    PublicationType.FINE_INFRACTION: FineInfractionSchema(),
    PublicationType.SEIZURE_INFRACTION: SeizureInfractionSchema(),
    PublicationType.GRANT_PROCESS: GrantProcessSchema(),
    PublicationType.PROCESS_EXTINCTION: ProcessExtinctionSchema(),
    PublicationType.NOTIFICATION_NOTICE: NotificationNotice(),
    PublicationType.SIMPLIFIED_ENVIRONMENTAL_LICENSE: SimplifiedEnvironmentalLicenseSchema(), # noqa
    PublicationType.DEADLINE_EXTENSION: DeadlineExtensionSchema(),
    PublicationType.RECTIFICATION: RectificationSchema(),
    PublicationType.ORDER_REVOCATION: OrderRevocationSchema(),
    PublicationType.SEIZURE: SeizureSchema(),
    PublicationType.DEGRADED_AREA_RECOVERY_PLAN: DegradedAreaRecoveryPlanSchema(), # noqa
    PublicationType.GRANT_ENVIRONMENTAL_LICENSE: GrantEnvironmentalLicenseSchema(), # noqa
    PublicationType.CONFORMITY_CERTIFICATE: ConformityCertificateSchema(),
    PublicationType.ICMBIO_INFRACTION_NOTICE: ICMBioInfractionNoticeSchema(),
    PublicationType.IBAMA_INFRACTION_NOTICE: IbamaInfractionNoticeSchema(),
    PublicationType.RIGHT_USE_WATER_RESOURCES_RENOVATION: RightUseWaterResourcesRenovationSchema(), # noqa
    PublicationType.RIGHT_USE_WATER_RESOURCES_CHANGE: RightUseWaterResourceChangeSchema() # noqa
}
