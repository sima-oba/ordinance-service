class UnionMemberMixin:
    def dump(self, *arg, **kwargs):
        """Raise if obj is not valid, will make union skip to next member."""
        errors = self.validate(*arg, **kwargs)
        if errors:
            raise ValueError(errors)
        return super().dump(*arg, **kwargs)
