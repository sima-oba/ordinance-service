from enum import Enum

from .alteration_license import AlterationLicense
from .animal_handling import AnimalHandling
from .cancel_ordinance import CancelOrdinance
from .condition_review import ConditionReview
from .environmental_authorization import EnvironmentalAuthorization
from .erratum import Erratum
from .exploration_approval import ExplorationApproval
from .extended_term import ExtendedTerm
from .forest_management import ForestManagement
from .forest_replacement_credit import ForestReplacementCredit
from .forest_volume_credit import ForestVolumeCredit
from .forest_volume_recognition import ForestVolumeRecognition
from .forest_volume_transfer import ForestVolumeTransfer
from .grant_waiver import GrantWaiver
from .installation_license import InstallationLicense
from .license_cancellation import LicenseCancellation
from .license_renewal import LicenseRenewal
from .license_revocation import LicenseRevocation
from .location_license import LocationLicense
from .operation_license import OperationLicense
from .owner_name_change import OwnerNameChange
from .ownership_transfer import OwnershipTransfer
from .planting_anticipation import PlantingAnticipation
from .preliminary_license import PreliminaryLicense
from .regularization_license import RegularizationLicense
from .right_use_water_resources import RightUseWaterResources
from .right_use_water_renovation import RightUseWaterResourcesRenovation
from .special_procedure import SpecialProcedure
from .unified_license import UnifiedLicense
from .vegetal_suppression import VegetalSuppression
from .owner_correction import OwnerCorrection
from .implantation_license import ImplantationLicense
from .infraction_warning import InfractionWarning
from .interdiction_infraction import InterdictionInfraction
from .demolition_penalty import DemolitionPenalty
from .fine_infraction import FineInfraction
from .seizure_infraction import SeizureInfraction
from .active_debt import ActiveDebit
from .grant_process import GrantProcess
from .process_extinction import ProcessExtinction
from .anticipated_environ_license import AnticipatedEnvironmentalLicense
from .notification_notice import NotificationNotice
from .simplified_environmental_license import SimplifiedEnvironmentalLicense
from .deadline_extension import DeadlineExtension
from .rectification import Rectification
from .order_revocation import OrderRevocation
from .seizure import Seizure
from .degraded_area_recovery_plan import DegradedAreaRecoveryPlan
from .grant_environmental_licenses import GrantEnvironmentalLicense
from .administrative_decision import AdministrativeDecision
from .conformity_certificate import ConformityCertificate
from .icmbio_infraction_notice import ICMBioInfractionNotice
from .ibama_infraction_notice import IbamaInfractionNotice

__all__ = [
    'AlterationLicense',
    'AnimalHandling',
    'CancelOrdinance',
    'ConditionReview',
    'EnvironmentalAuthorization',
    'Erratum',
    'ExplorationApproval',
    'ExtendedTerm',
    'ForestManagement',
    'ForestReplacementCredit',
    'ForestVolumeCredit',
    'ForestVolumeRecognition',
    'ForestVolumeTransfer',
    'GrantWaiver',
    'InstallationLicense',
    'LicenseCancellation',
    'LicenseRenewal',
    'LicenseRevocation',
    'LocationLicense',
    'OperationLicense',
    'OwnerNameChange',
    'OwnershipTransfer',
    'PlantingAnticipation',
    'PreliminaryLicense',
    'RegularizationLicense',
    'RightUseWaterResources',
    'RightUseWaterResourcesRenovation',
    'SpecialProcedure',
    'UnifiedLicense',
    'VegetalSuppression',
    'OwnerCorrection',
    'ImplantationLicense',
    'InfractionWarning',
    'InterdictionInfraction',
    'DemolitionPenalty',
    'FineInfraction',
    'SeizureInfraction',
    'ActiveDebit',
    'GrantProcess',
    'ProcessExtinction',
    'AnticipatedEnvironmentalLicense',
    'NotificationNotice',
    'SimplifiedEnvironmentalLicense',
    'DeadlineExtension',
    'Rectification',
    'OrderRevocation',
    'Seizure',
    'DegradedAreaRecoveryPlan',
    'GrantEnvironmentalLicense',
    'AdministrativeDecision',
    'ConformityCertificate',
    'ICMBioInfractionNotice',
    'IbamaInfractionNotice'
]


class PublicationType(Enum):
    ALTERATION_LICENSE = 'Licença de Alteração'
    ANIMAL_HANDLING = 'Autorização para Manejo de Fauna'
    CANCEL_ = 'Cancelamento'
    CONDITION_REVIEW = 'Revisão de Condicionante'
    ENVIRONMENTAL_AUTHORIZATION = 'Autorização Ambiental'
    ERRATUM = 'Errata'
    EXPLORATION_APPROVAL = 'Aprovação da Exploração ou Corte de Florestas Plantadas'  # noqa
    EXTENDED_TERM = 'Conceder Prorrogação de Prazo de Validade'
    FOREST_MANAGEMENT = 'FOREST_MANAGEMENT'
    FOREST_REPLACEMENT_CREDIT = 'Emissão de Crédito de Reposição Florestal'
    FOREST_VOLUME_CREDIT = 'Emissão de Crédito Florestal'
    FOREST_VOLUME_RECOGNITION = 'Reconhecimento de Volume Florestal'
    FOREST_VOLUME_TRANSFER = 'Transferência de Crédito de Volume Florestal'
    GRANT_WAIVER = 'GRANT_WAIVER'
    INSTALLATION_LICENSE = 'Licença de Instalação'
    LICENSE_CANCELLATION = 'Cancelamento de Licença'
    LICENSE_RENEWAL = 'Renovação de Licença'
    LICENSE_REVOCATION = 'Revogação de Licença'
    OPERATION_LICENSE = 'Licença de Operação'
    OWNER_NAME_CHANGE = 'Alteração da Razão Social'
    OWNERSHIP_TRANSFER = 'Transferência de Titularidade'
    PLANTING_ANTICIPATION = 'Antecipacao de Plantio'
    PRELIMINARY_LICENSE = 'PRELIMINARY_LICENSE'
    REGULARIZATION_LICENSE = 'Licença de Regularização'
    RIGHT_USE_WATER_RESOURCES = 'Outorga do Direito de Uso dos Recursos Hídricos'  # noqa
    SPECIAL_PROCEDURE = 'Autorização por Procedimento Especial'
    UNIFIED_LICENSE = 'Licença Unificada'
    VEGETAL_SUPPRESSION = 'Autorização de Supressão de Vegetação Nativa'
    LOCATION_LICENSE = 'Licença de Localização'
    OWNER_CORRECTION = 'Retífica da Razão Social'
    IMPLANTATION_LICENSE = 'Licença de Implantação'
    INFRACTION_WARNING = 'Auto de Infração de Advertência'
    INTERDICTION_INFRACTION = 'Embargo e Interdição'
    DEMOLITION_PENALTY = 'Auto de Infração de Interdição'
    FINE_INFRACTION = 'Auto de Infração de Multa'
    SEIZURE_INFRACTION = 'Auto de Infração de Apreensão'
    ACTIVE_DEBIT = 'Dívida Ativa'
    GRANT_PROCESS = 'Análise de Processo de Outorga'
    PROCESS_EXTINCTION = 'Extinção de Processo'
    ANTICIPATED_ENVIRONMENTAL_LICENSE = ''
    NOTIFICATION_NOTICE = 'Licença Ambiental Prévial'
    SIMPLIFIED_ENVIRONMENTAL_LICENSE = 'Licença Simplificada'
    DEADLINE_EXTENSION = 'Prorrogação de Prazo de Validade'
    RECTIFICATION = 'Retificação de Portaria'
    ORDER_REVOCATION = 'Revogação Licença'
    SEIZURE = 'Interdição'
    DEGRADED_AREA_RECOVERY_PLAN = 'Plano de Recuperação de Área Degradada'
    GRANT_ENVIRONMENTAL_LICENSE = 'GRANT_ENVIRONMENTAL_LICENSE'
    ADMINISTRATIVE_DECISION = 'Decisão Administrativa'
    CONFORMITY_CERTIFICATE = 'Certidão de Conformidade de Uso e Ocupação do Solo'  # noqa
    ICMBIO_INFRACTION_NOTICE = 'Autos de Infração Emitidos pelo ICMBio'
    IBAMA_INFRACTION_NOTICE = 'Autos de Infração Emitidos Pelo IBAMA'
    LICENSE_DISMISSAL = 'Dispensa de Licença Ambiental'
    LEGAL_RESERVE_LOCATION_APPROVAL = 'Aprovação de Localização de Reserva Legal'  # noqa
    TEMPORARY_INTERDICTION_NOTICE = 'Auto de Infração de Interdição Temporária'  # noqa
    PROCESS_ANALYSIS = 'Análise de Processo'
    PLANT_ENRICHMENT_PLAN = 'Plano de Enriquecimento Vegetal'
    TEMPORARY_SEIZURE = 'Embargo Temporário'
    PENALTY_WARNING = 'Penalidade de Advertência'
    CEFIR = 'Cadastro Estadual Florestal de Imóveis Rurais'
    SOLID_WASTE_MANAGEMENT_PLAN = 'Programa de Gerenciamento de Resíduos Sólidos'  # noqa
    RIGHT_USE_WATER_RESOURCES_RENOVATION = 'Renovação da Outorga do Direito de Uso dos Recursos Hídricos'  # noqa
    RIGHT_USE_WATER_RESOURCES_CHANGE = 'Alteração da Outorga do Direito de Uso dos Recursos Hídricos'  # noqa
    VOLUME_EXPASION = 'Ampliação do volume'
    PREVENTIVE = 'Preventiva'
    TEMPORARY_SUSPEND = 'Suspender Temporariamente'
