// SPDX-License-Identifier: Apache-2.0
// Copyright 2024 The Foundry Visionmongers Ltd
#include <algorithm>
#include <optional>
#include <string>
#include <string_view>

#include <export.h>

#include <openassetio/errors/exceptions.hpp>
#include <openassetio/managerApi/EntityReferencePagerInterface.hpp>
#include <openassetio/managerApi/ManagerInterface.hpp>
#include <openassetio/pluginSystem/CppPluginSystemManagerPlugin.hpp>
#include <openassetio/trait/TraitsData.hpp>

#include <openassetio_mediacreation/traits/content/LocatableContentTrait.hpp>

namespace {
// Unique ID of the plugin. Must match that advertised by the partner
// Python plugin.
constexpr std::string_view kPluginId = "org.openassetio.examples.simplehybridmanager";
// The one and only entity reference we support. These two lines
// represent our backend database.
constexpr std::string_view kTheEntityReference = "examplehybrid://example_entity";
constexpr std::string_view kTheEntityPath = "file:///some/path.exr";
}  // namespace

/**
 * C++ side of Simple Hybrid Manager.
 */
struct SimpleHybridManagerInterface final : openassetio::managerApi::ManagerInterface {
  /**
   * Identifier must match the partner Python plugin's identifier.
   */
  [[nodiscard]] openassetio::Identifier identifier() const override {
    return openassetio::Identifier{kPluginId};
  }

  /**
   * displayName has no base class implementation so must be
   * implemented.
   *
   * This display name will be used if the C++ plugin system takes
   * precedence in the hybrid plugin system.
   */
  [[nodiscard]] openassetio::Str displayName() const override { return "Simple Hybrid Manager"; }

  /**
   * The C++ side of this hybrid plugin is solely responsible for
   * `resolve` and nothing else.
   */
  [[nodiscard]] bool hasCapability(const Capability capability) override {
    return capability == Capability::kResolution;
  }

  /**
   * Implementation of `resolve` in C++ - the only capability supported
   * by this plugin. Other capabilities are handled by the partner
   * Python plugin.
   */
  void resolve(const openassetio::EntityReferences& entityReferences,
               const openassetio::trait::TraitSet& traitSet,
               const openassetio::access::ResolveAccess resolveAccess,
               [[maybe_unused]] const openassetio::ContextConstPtr& context,
               [[maybe_unused]] const openassetio::managerApi::HostSessionPtr& hostSession,
               const ResolveSuccessCallback& successCallback,
               const BatchElementErrorCallback& errorCallback) override {
    using openassetio::EntityReference;
    using openassetio::access::ResolveAccess;
    using openassetio::errors::BatchElementError;
    using openassetio::trait::TraitsData;
    using openassetio::trait::TraitsDataPtr;
    using openassetio_mediacreation::traits::content::LocatableContentTrait;

    // We only support read access.
    if (resolveAccess != ResolveAccess::kRead) {
      for (std::size_t idx = 0; idx < entityReferences.size(); ++idx) {
        errorCallback(idx, BatchElementError{BatchElementError::ErrorCode::kEntityAccessError,
                                             "Entity access is read-only"});
      }
      return;
    }

    // Loop each entity reference in the input batch.
    for (std::size_t idx = 0; idx < entityReferences.size(); ++idx) {
      // We only support one entity.
      if (entityReferences[idx].toString() == kTheEntityReference) {
        TraitsDataPtr traitsData = TraitsData::make();

        // Populate the requested traits with their properties. We only
        // support one trait.
        if (traitSet.count(LocatableContentTrait::kId)) {
          LocatableContentTrait{traitsData}.setLocation(openassetio::Str{kTheEntityPath});
        }

        successCallback(idx, std::move(traitsData));
      } else {
        // If we can't find the entity reference in the database, then
        // flag an error.
        errorCallback(idx, BatchElementError{BatchElementError::ErrorCode::kEntityResolutionError,
                                             "Entity not found"});
      }
    }
  }
};

/**
 * Subclass of the CppPluginSystemManagerPlugin that can be used to
 * construct instances of our simple ManagerInterface.
 */
struct SimpleHybridManagerPlugin final : openassetio::pluginSystem::CppPluginSystemManagerPlugin {
  [[nodiscard]] openassetio::Identifier identifier() const override {
    return openassetio::Identifier{kPluginId};
  }
  openassetio::managerApi::ManagerInterfacePtr interface() override {
    return std::make_shared<SimpleHybridManagerInterface>();
  }
};

extern "C" {
/**
 * External entry point that the OpenAssetIO plugin system will query.
 */
OPENASSETIO_EXAMPLE_SIMPLEHYBRIDMANAGER_EXPORT
openassetio::pluginSystem::PluginFactory openassetioPlugin() noexcept {
  return []() noexcept -> openassetio::pluginSystem::CppPluginSystemPluginPtr {
    return std::make_shared<SimpleHybridManagerPlugin>();
  };
}
}
