# frozen_string_literal: true

class Souvenir
  include ActiveModel::Model
  attr_accessor(
    :primaryImageSmall,
    :title,
    :culture,
    :objectDate,
    :artistDisplayName
  )
end
