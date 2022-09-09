from .publication_type import (
    PublicationType,
    AlterationLicense,
    AnimalHandling,
    CancelOrdinance,
    ConditionReview,
    EnvironmentalAuthorization,
    Erratum,
    ExplorationApproval,
    ExtendedTerm,
    ForestManagement,
    ForestReplacementCredit,
    ForestVolumeCredit,
    ForestVolumeRecognition,
    ForestVolumeTransfer,
    GrantWaiver,
    InstallationLicense,
    LicenseCancellation,
    LicenseRenewal,
    LicenseRevocation,
    OperationLicense,
    OwnerNameChange,
    OwnershipTransfer,
    PlantingAnticipation,
    PreliminaryLicense,
    RegularizationLicense,
    RightUseWaterResources,
    SpecialProcedure,
    UnifiedLicense,
    VegetalSuppression,
    LocationLicense,
    OwnerCorrection,
    ImplantationLicense,
    InfractionWarning,
    InterdictionInfraction,
    DemolitionPenalty,
    FineInfraction,
    SeizureInfraction,
    ActiveDebit,
    GrantProcess,
    ProcessExtinction,
    AnticipatedEnvironmentalLicense,
    NotificationNotice,
    SimplifiedEnvironmentalLicense,
    DeadlineExtension,
    Rectification,
    OrderRevocation,
    Seizure,
    DegradedAreaRecoveryPlan,
    GrantEnvironmentalLicense,
    AdministrativeDecision,
    ConformityCertificate,
    ICMBioInfractionNotice,
    IbamaInfractionNotice
)
from .model import Model

from dataclasses import dataclass
from datetime import datetime
from typing import Union, Optional


@dataclass
class Publication(Model):
    ordinance_number: str
    ordinance_type: PublicationType
    title: str
    publish_date: datetime
    issuer: str
    issuer_name: str
    owner_doc: str
    owner_name: str
    term: Optional[str]
    process: str
    notes: Optional[str]
    link: Optional[str]
    details: Union[
        AlterationLicense,
        AnimalHandling,
        CancelOrdinance,
        ConditionReview,
        EnvironmentalAuthorization,
        Erratum,
        ExplorationApproval,
        ExtendedTerm,
        ForestManagement,
        ForestReplacementCredit,
        ForestVolumeCredit,
        ForestVolumeRecognition,
        ForestVolumeTransfer,
        GrantWaiver,
        InstallationLicense,
        LicenseCancellation,
        LicenseRenewal,
        LicenseRevocation,
        OperationLicense,
        OwnerNameChange,
        OwnershipTransfer,
        PlantingAnticipation,
        PreliminaryLicense,
        RegularizationLicense,
        RightUseWaterResources,
        SpecialProcedure,
        UnifiedLicense,
        VegetalSuppression,
        LocationLicense,
        OwnerCorrection,
        ImplantationLicense,
        InfractionWarning,
        InterdictionInfraction,
        DemolitionPenalty,
        FineInfraction,
        SeizureInfraction,
        ActiveDebit,
        GrantProcess,
        ProcessExtinction,
        AnticipatedEnvironmentalLicense,
        NotificationNotice,
        SimplifiedEnvironmentalLicense,
        DeadlineExtension,
        Rectification,
        OrderRevocation,
        Seizure,
        DegradedAreaRecoveryPlan,
        GrantEnvironmentalLicense,
        AdministrativeDecision,
        ConformityCertificate,
        ICMBioInfractionNotice,
        IbamaInfractionNotice
    ]

    def is_valid(self) -> None:
        pass

    @staticmethod
    def linkage(**kwargs: dict) -> str:
        for key in kwargs.keys():
            if key.startswith('ordinance_number_'):
                return key
