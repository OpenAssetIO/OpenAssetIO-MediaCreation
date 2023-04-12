// SPDX-License-Identifier: Apache-2.0
// Copyright 2022 The Foundry Visionmongers Ltd

// Include all headers to test they are where we expect and can be
// compiled.

#include <openassetio_mediacreation/openassetio_mediacreation.hpp>
#include <openassetio_mediacreation/traits/content.hpp>
#include <openassetio_mediacreation/traits/content/LocatableContentTrait.hpp>
#include <openassetio_mediacreation/traits/identity/DisplayNameTrait.hpp>
#include <openassetio_mediacreation/traits/managementPolicy.hpp>
#include <openassetio_mediacreation/traits/managementPolicy/ManagedTrait.hpp>
#include <openassetio_mediacreation/traits/managementPolicy/ResolvesFutureEntitiesTrait.hpp>
#include <openassetio_mediacreation/traits/timeline.hpp>
#include <openassetio_mediacreation/traits/timeline/ClipTrait.hpp>
#include <openassetio_mediacreation/traits/timeline/TimelineTrait.hpp>
#include <openassetio_mediacreation/traits/timeline/TrackTrait.hpp>
#include <openassetio_mediacreation/traits/traits.hpp>

using namespace openassetio_mediacreation;

int main() {
  auto traits = openassetio::TraitsData::make();
  auto trait = traits::managementPolicy::ManagedTrait(traits);
  trait.imbue();
  return 0;
}
